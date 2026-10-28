# 💬 Intelligent FAQ Support Assistant

An end-to-end NLP-powered FAQ assistant built with Python, NLTK, and scikit-learn. It uses text normalization, tokenization, lemmatization, and TF-IDF cosine similarity to match customer questions against curated intents in real time, served via a Streamlit chat UI.

---

### 🌐 Live Demo
Access the live application here:  
👉 **[FAQ Chatbot on Streamlit Cloud](https://faq-chatbot-z8ko2wrqhn9vbzidrmyjrq.streamlit.app/)**

---

## ✨ Features

- **Text Preprocessing Pipeline:** Case normalization, punctuation removal, stop-word filtering, and WordNet lemmatization using NLTK.
- **Intent Vectorization & Matching:** Scikit-learn TF-IDF vectorizer paired with cosine similarity scoring for query classification.
- **Confidence Scoring:** Real-time visibility into engine confidence (e.g., *94% match*).
- **Interactive Sidebar UX:** Quick-suggestion prompt buttons for common questions and a one-click chat history reset.
- **Fallback & Escalation Workflow:** Captures unhandled or low-confidence questions into an administrative log (`unanswered_logs.json`) while presenting immediate human-support contact options.
- **Automated CI/CD Pipeline:** GitHub Actions workflow executing unit tests on every push, coupled with automatic continuous deployment via Streamlit Community Cloud.

---

## 🛠️ Tech Stack

- **Language:** Python
- **Natural Language Processing:** NLTK (`punkt`, `stopwords`, `wordnet`)
- **Machine Learning:** scikit-learn (TF-IDF Vectorization, Cosine Similarity)
- **Frontend / Deployment:** Streamlit, Streamlit Community Cloud
- **CI/CD:** GitHub Actions

---

## 📂 Project Structure

```text
├── .github/workflows/
│   └── ci.yml               # Automated test pipeline
├── app.py                   # Streamlit chat interface and sidebar actions
├── nlp_engine.py            # Text preprocessing, TF-IDF vectorizer, and matching logic
├── test_engine.py           # Automated unit tests for engine validation
├── faqs.json                # Knowledge base containing intents, patterns, and answers
├── requirements.txt         # Core dependencies
└── README.md                # Project documentation
