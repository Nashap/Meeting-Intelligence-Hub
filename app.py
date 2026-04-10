from flask import Flask, render_template, request, redirect, Response
import os
from textblob import TextBlob

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# ---------- Extract ----------
def extract_actions(text):
    actions = []
    decisions = []

    for line in text.split('.'):
        line = line.strip()

        if any(word in line.lower() for word in ["decided", "agreed", "finalized"]):
            decisions.append(line)

        if any(word in line.lower() for word in ["will", "should", "assign", "task"]):
            actions.append(line)

    return decisions, actions

# ---------- Sentiment ----------
def get_sentiment(text):
    polarity = TextBlob(text).sentiment.polarity

    if polarity > 0:
        return "Positive 😊"
    elif polarity < 0:
        return "Negative 😡"
    else:
        return "Neutral 😐"

# ---------- Highlight ----------
def highlight_keywords(sentence, query_words):
    for word in query_words:
        sentence = sentence.replace(word, f"<mark>{word}</mark>")
    return sentence

# ---------- Chatbot ----------
def ask_chatbot(query, transcript):
    query_words = query.lower().split()
    sentences = transcript.split('.')

    results = []

    for sentence in sentences:
        sentence_lower = sentence.lower()

        if any(word in sentence_lower for word in query_words):
            highlighted = highlight_keywords(sentence, query_words)
            results.append(f"👉 {highlighted.strip()}")

    # Special logic for decisions
    if "decision" in query.lower():
        for sentence in sentences:
            if "decided" in sentence.lower() or "agreed" in sentence.lower():
                results.append(f"👉 {sentence.strip()}")

    results = list(set(results))

    if results:
        return "<br>".join(results[:3])
    else:
        return "No relevant information found."

# ---------- Summary ----------
def generate_summary(text):
    sentences = text.split('.')[:3]
    return ". ".join(sentences) + "."

# ---------- Speaker Detection ----------
def get_speakers(text):
    speakers = set()
    for line in text.split('\n'):
        if ":" in line:
            speaker = line.split(":")[0]
            speakers.add(speaker)
    return list(speakers)

# ---------- Routes ----------
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files.get("file")

    if not file:
        return redirect("/")

    filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(filepath)

    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()

    decisions, actions = extract_actions(text)
    sentiment = get_sentiment(text)
    summary = generate_summary(text)
    speakers = get_speakers(text)

    return render_template(
        "dashboard.html",
        transcript=text,
        decisions=decisions,
        actions=actions,
        sentiment=sentiment,
        summary=summary,
        speakers=speakers
    )

@app.route("/chat", methods=["POST"])
def chat():
    query = request.form.get("query")
    transcript = request.form.get("transcript")

    return ask_chatbot(query, transcript)

# ---------- CSV Download ----------
@app.route("/download")
def download():
    decisions = request.args.getlist("decisions")
    actions = request.args.getlist("actions")

    def generate():
        yield "Type,Content\n"
        for d in decisions:
            yield f"Decision,{d}\n"
        for a in actions:
            yield f"Action,{a}\n"

    return Response(generate(), mimetype="text/csv",
                    headers={"Content-Disposition": "attachment;filename=report.csv"})

# ---------- Run ----------
if __name__ == "__main__":
    app.run(debug=True)