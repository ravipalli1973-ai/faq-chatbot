import json
import string
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)
nltk.download('stopwords', quiet=True)
nltk.download('wordnet', quiet=True)

lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

def preprocess(text: str) -> str:
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    tokens = word_tokenize(text)
    cleaned_tokens = [
        lemmatizer.lemmatize(token)
        for token in tokens
        if token not in stop_words
    ]
    return " ".join(cleaned_tokens)

class FAQMatcher:
    def __init__(self, faq_file="faqs.json"):
        with open(faq_file, "r", encoding="utf-8-sig") as f:
            self.faq_data = json.load(f)

        self.patterns = []
        self.pattern_to_answer = []

        for item in self.faq_data:
            answer = item["answer"]
            for pattern in item["patterns"]:
                self.patterns.append(preprocess(pattern))
                self.pattern_to_answer.append(answer)

        self.vectorizer = TfidfVectorizer()
        self.faq_matrix = self.vectorizer.fit_transform(self.patterns)

    def get_response_with_confidence(self, user_query: str, threshold: float = 0.20):
        cleaned_query = preprocess(user_query)
        if not cleaned_query.strip():
            return "Please provide more detail in your question so I can assist you.", 0.0

        query_vector = self.vectorizer.transform([cleaned_query])
        similarities = cosine_similarity(query_vector, self.faq_matrix)[0]

        best_index = similarities.argmax()
        highest_score = float(similarities[best_index])

        if highest_score < threshold:
            return "I'm sorry, I couldn't find an answer matching your question. Please try rephrasing or contact support.", round(highest_score * 100, 1)

        return self.pattern_to_answer[best_index], round(highest_score * 100, 1)

if __name__ == "__main__":
    matcher = FAQMatcher()
    sample = "when do you open and close?"
    reply, score = matcher.get_response_with_confidence(sample)
    print(f"Sample Query: {sample}")
    print(f"Chatbot Match: {reply} (Confidence: {score}%)")
