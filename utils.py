def highlight_skills(resume_text, skills):
    matched = [skill for skill in skills if skill.lower() in resume_text.lower()]
    return matched