import PyPDF2
import re

def extract_text_from_pdf(file_path):
    """Extracts text from a PDF file."""
    with open(file_path, 'rb') as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        text = ''.join(page.extract_text() for page in reader.pages)
    return text

def extract_skills(text, skills_list):
    """Extracts matching skills from text."""
    skills = [skill for skill in skills_list if skill.lower() in text.lower()]
    return skills

def extract_contact_info(text):
    """Extracts phone number and email from text."""
    phone = re.findall(r'\b\d{10}\b', text)
    email = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)
    return {'phone': phone[0] if phone else None, 'email': email[0] if email else None}
