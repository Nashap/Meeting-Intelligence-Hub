#  Meeting Intelligence Hub

An AI-powered web application that transforms meeting transcripts into **actionable insights** using Natural Language Processing.

---

##  Demo

 Demo Video: *(Add your video link here)*

---

##  Screenshots
<img width="1353" height="553" alt="image" src="https://github.com/user-attachments/assets/57352624-4e15-4974-a6dc-6410ffea1e56" />
<img width="1324" height="553" alt="image" src="https://github.com/user-attachments/assets/11ec8dd9-eaf7-4194-8b9d-2257cd8d0b12" />
<img width="1303" height="558" alt="image" src="https://github.com/user-attachments/assets/c12004f8-94be-4fd3-a8dc-cfafb0af99af" />
<img width="1325" height="552" alt="image" src="https://github.com/user-attachments/assets/58af475f-493b-46e8-a1a3-55683da8bd52" />
<img width="1319" height="551" alt="image" src="https://github.com/user-attachments/assets/1eca7390-90a9-4a0d-b367-f999565ef063" />
<img width="1310" height="532" alt="image" src="https://github.com/user-attachments/assets/e2ad09a2-21eb-41da-91d7-1a28dbf50cf3" />
<img width="1316" height="550" alt="image" src="https://github.com/user-attachments/assets/ab4f00a1-a19e-4142-8f52-abec35849a01" />
<img width="1323" height="530" alt="image" src="https://github.com/user-attachments/assets/c25559fa-6c53-4e4a-961e-e7d6085b8762" />
<img width="1315" height="537" alt="image" src="https://github.com/user-attachments/assets/2ae2a961-b130-4d37-b0e8-255d648f62de" />
<img width="601" height="378" alt="image" src="https://github.com/user-attachments/assets/fe883988-a494-4897-b7c8-46e1fbc5d5ee" />






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

##  Tech Stack

| Technology   | Purpose       |
| ------------ | ------------- |
| Flask        | Backend       |
| TextBlob     | NLP           |
| Tailwind CSS | UI            |
| JavaScript   | Interactivity |

---

##  How to Run

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

##  Future Improvements

*  Voice input
*  Charts dashboard
*  Export PDF
*  Advanced AI models (LLM)

---

##  Author

NASHA P
