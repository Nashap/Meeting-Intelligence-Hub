#  Meeting Intelligence Hub

An AI-powered web application that transforms meeting transcripts into **actionable insights** using Natural Language Processing.

---

##  Demo

 Demo Video: *(Add your video link here)*

---

##  Screenshots

### Upload Page

(Add screenshot)

### Dashboard

(Add screenshot)

### Chatbot

(Add screenshot)

---

##  Features

*  Upload meeting transcript (.txt)
*  Extract:

  * Decisions
  * Action Items
*  Sentiment Analysis
*  Chatbot (ask questions from transcript)
*  Structured dashboard (Who / What / By When)
*  Export insights as CSV

---

##  How It Works (AI Logic)

1. **Text Processing**

   * Transcript is split into sentences

2. **Decision Extraction**

   * Detects keywords like:

     * "decided", "agreed", "finalized"

3. **Action Extraction**

   * Detects:

     * "will", "should", "task"

4. **Sentiment Analysis**

   * Uses TextBlob polarity score

5. **Chatbot**

   * Matches user query with relevant sentences
   * Highlights keywords

---

## 🛠️ Tech Stack

| Technology   | Purpose       |
| ------------ | ------------- |
| Flask        | Backend       |
| TextBlob     | NLP           |
| Tailwind CSS | UI            |
| JavaScript   | Interactivity |

---

## ▶️ How to Run

```bash
pip install -r requirements.txt
python app.py
```

Open browser:

```
http://127.0.0.1:5000
```

---

##  Project Structure

```
Meeting-Intelligence/
│── app.py
│── templates/
│   ├── index.html
│   ├── dashboard.html
│── uploads/
│── requirements.txt
│── README.md
```

---

##  Sample Output

### Decisions

* Project timeline finalized
* Budget approved

### Actions

* John: Prepare report by Friday
* Team: Complete testing

---

## 🚀 Future Improvements

*  Voice input
*  Charts dashboard
*  Export PDF
*  Advanced AI models (LLM)

---

## 👨 Author

NASHA P
