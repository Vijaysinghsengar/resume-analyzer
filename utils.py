from PyPDF2 import PdfReader

def extract_text(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text.lower()

skills_list = [
    "python","sql","machine learning","excel","power bi",
    "java","react","cloud","data science","ai"
]

def extract_skills(text):
    found = []
    for skill in skills_list:
        if skill in text:
            found.append(skill)
    return found

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_score(resume, job_desc):
    tfidf = TfidfVectorizer()
    vectors = tfidf.fit_transform([resume, job_desc])
    score = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]
    return round(score * 100, 2)

def recommend_companies(user_skills, companies):
    results = []

    for company in companies:
        match = len(set(user_skills) & set(company["skills"]))
        score = match / len(company["skills"])

        results.append((company["name"], score, company["type"]))

    results.sort(key=lambda x: x[1], reverse=True)
    return results[:5]