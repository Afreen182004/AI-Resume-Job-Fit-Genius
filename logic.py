import re
import numpy as np

def calculate_skill_confidence(resume_text, skill_list):
    text = resume_text.lower()
    confidence = {}
    for skill in skill_list:
        if skill in text:
            confidence[skill] = 70 + (len(skill) % 25)
        else:
            confidence[skill] = 0
    return confidence


def calculate_skill_gap(resume_text):
    skills_list = [
        "python", "sql", "machine learning", "deep learning",
        "excel", "powerbi", "nlp", "statistics", "cloud"
    ]
    text = resume_text.lower()
    gap_score = {}
    total_gap = 0
    for skill in skills_list:
        if skill in text:
            gap_score[skill] = 0
        else:
            gap = np.random.randint(5, 20)
            gap_score[skill] = gap
            total_gap += gap
    return gap_score, total_gap


JOB_ROLE_SKILLS = {
    "Data Analyst": ["python", "sql", "excel", "powerbi", "statistics"],
    "Data Scientist": ["python", "machine learning", "statistics", "nlp"],
    "ML Engineer": ["python", "machine learning", "deep learning"],
    "Business Analyst": ["excel", "sql", "dashboard", "business"]
}

def calculate_role_match(resume_text):
    text = resume_text.lower()
    scores = {}
    for role, skills in JOB_ROLE_SKILLS.items():
        match = sum(1 for s in skills if s in text)
        scores[role] = int((match / len(skills)) * 100)
    return scores


STRENGTH_KEYWORDS = {
    "Analytical Thinking": ["analysis", "statistics", "problem"],
    "Programming Skills": ["python", "coding", "development"],
    "Machine Learning": ["machine learning", "model"],
    "Communication": ["presentation", "report"]
}

def generate_strength_summary(resume_text):
    text = resume_text.lower()
    strengths = []
    for strength, keywords in STRENGTH_KEYWORDS.items():
        if any(k in text for k in keywords):
            strengths.append(strength)
    if not strengths:
        return "No strong technical strengths detected."
    return "Strong areas: " + ", ".join(strengths)


WEAKNESS_KEYWORDS = {
    "Cloud Computing": ["aws", "azure", "gcp"],
    "Deep Learning": ["deep learning", "cnn", "rnn"],
    "Big Data": ["spark", "hadoop"]
}

def generate_weakness_summary(resume_text):
    text = resume_text.lower()
    missing = []
    for area, keywords in WEAKNESS_KEYWORDS.items():
        if not any(k in text for k in keywords):
            missing.append(area)
    if not missing:
        return "No major technical gaps found."
    return "Missing exposure in: " + ", ".join(missing)


def calculate_consistency(resume_text):
    text = resume_text.lower()
    skills = ["python", "sql", "excel", "machine learning"]
    projects = ["project", "internship", "developed"]
    skill_score = sum(1 for s in skills if s in text)
    project_score = sum(1 for p in projects if p in text)
    numbers = len(re.findall(r'\d+', text))
    total = len(skills) + len(projects) + 3
    score = ((skill_score + project_score + min(numbers, 3)) / total) * 100
    return round(score, 2)


ATS_KEYWORDS = {
    "Programming": ["python", "java", "sql"],
    "Data": ["machine learning", "statistics"],
    "Tools": ["git", "powerbi", "tableau"],
    "Cloud": ["aws", "azure"],
    "Soft Skills": ["communication", "team"]
}

def calculate_ats_score(resume_text):
    text = resume_text.lower()
    matched = 0
    details = {}
    for category, keywords in ATS_KEYWORDS.items():
        if any(k in text for k in keywords):
            matched += 1
            details[category] = "Matched"
        else:
            details[category] = "Missing"
    ats_score = int((matched / len(ATS_KEYWORDS)) * 100)
    return ats_score, details


def jd_resume_match(resume_text, job_text):
    resume_text = resume_text.lower()
    job_text = job_text.lower()
    job_skills = ["python", "sql", "machine learning", "excel", "powerbi", "nlp"]
    matched = []
    missing = []
    for skill in job_skills:
        if skill in resume_text:
            matched.append(skill)
        elif skill in job_text:
            missing.append(skill)
    fit_score = (len(matched) / len(job_skills)) * 100
    return matched, missing, round(fit_score, 2)
def generate_skill_timeline(resume_text):
    import re

    SKILLS = [
        "python", "java", "sql", "machine learning", "deep learning",
        "data analysis", "powerbi", "tableau", "excel", "aws", "azure",
        "html", "css", "javascript", "flask", "django"
    ]

    text = resume_text.lower()

    years = re.findall(r'(19\d{2}|20\d{2})', text)

    timeline = []

    for i in range(len(years) - 1):
        start_year = years[i]
        end_year = years[i + 1]

        for skill in SKILLS:
            if skill in text:
                timeline.append(f"{start_year}–{end_year} → {skill}")

    timeline = list(set(timeline))

    if len(timeline) == 0:
        return ["No skill timeline detected"]

    return timeline
def recommend_jobs_from_jd(job_text):
    job_text = job_text.lower()

    JOB_LIBRARY = {
        "Data Analyst": ["python", "sql", "excel", "powerbi", "statistics", "visualization"],
        "Data Scientist": ["python", "machine learning", "statistics", "nlp", "deep learning"],
        "ML Engineer": ["python", "machine learning", "deep learning", "tensorflow", "pytorch"],
        "Business Analyst": ["excel", "sql", "dashboard", "business", "communication"],
        "Software Developer": ["python", "java", "git", "api", "database"]
    }

    recommendations = {}

    for role, skills in JOB_LIBRARY.items():
        match_count = 0
        for skill in skills:
            if skill in job_text:
                match_count += 1

        score = int((match_count / len(skills)) * 100)
        if score > 0:
            recommendations[role] = score

    recommendations = dict(
        sorted(recommendations.items(), key=lambda x: x[1], reverse=True)
    )

    return recommendations

def final_candidate_decision(ats_score, jd_fit, consistency):
    if ats_score >= 70 and jd_fit >= 60 and consistency >= 60:
        return "SELECT"
    elif ats_score >= 50 and jd_fit >= 40:
        return "WAITING"
    else:
        return "REJECT"

