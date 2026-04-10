#  Approach Document – Meeting Intelligence Hub

## 1. Problem Statement

Meetings generate large volumes of unstructured text data in the form of transcripts.
Extracting useful insights such as decisions, action items, and key points manually is time-consuming and inefficient.

---

## 2. Proposed Solution

We developed an AI-powered web application that:

* Accepts meeting transcript files as input
* Automatically extracts:

  * Decisions
  * Action Items
* Performs sentiment analysis
* Allows users to query the transcript using a chatbot
* Provides structured output in a dashboard
* Enables export of results as CSV

---

## 3. System Architecture

User → Upload Transcript → Flask Backend → NLP Processing → Dashboard UI

### Flow:

1. User uploads a `.txt` file
2. Backend reads the file
3. Text is processed using NLP techniques
4. Extracted data is displayed in UI
5. User interacts using chatbot or exports results

---

## 4. Key Components

### 4.1 Text Processing

* The transcript is split into sentences
* Each sentence is analyzed individually

### 4.2 Decision Extraction

* Uses keyword-based approach
* Detects words like:

  * "decided"
  * "agreed"
  * "finalized"

### 4.3 Action Item Extraction

* Identifies actionable sentences using:

  * "will"
  * "should"
  * "task"
* Extracts responsible person when possible

### 4.4 Sentiment Analysis

* Implemented using TextBlob
* Determines polarity:

  * Positive
  * Negative
  * Neutral

### 4.5 Chatbot

* Accepts user query
* Matches keywords with transcript sentences
* Returns relevant results
* Highlights matched terms

### 4.6 Export Feature

* Extracted insights are downloadable as CSV
* Helps in reporting and documentation

---

## 5. Tech Stack Justification

| Technology   | Reason                            |
| ------------ | --------------------------------- |
| Flask        | Lightweight backend framework     |
| TextBlob     | Simple NLP and sentiment analysis |
| Tailwind CSS | Fast and modern UI styling        |
| JavaScript   | Enables chatbot interaction       |

---

## 6. Limitations

* Uses keyword-based extraction (not fully context-aware)
* Limited understanding of complex queries
* Does not use advanced machine learning models

---

## 7. Future Improvements

* Integration with Large Language Models (LLMs)
* Better entity extraction (Who / When detection)
* Voice-based interaction
* PDF report generation
* Advanced analytics dashboard

---

## 8. Conclusion

The system successfully demonstrates how AI can transform unstructured meeting data into structured, actionable insights.
It improves productivity and reduces manual effort in analyzing meetings.
