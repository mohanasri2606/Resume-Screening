import numpy as np

def load_job_description(file_path):
    """Loads a job description from a text file."""
    with open(file_path, 'r') as file:
        return file.read()

def calculate_match_percentage(resume_skills, job_skills):
    """Calculates the match percentage between resume and job description skills."""
    match_count = len(set(resume_skills) & set(job_skills))  # Intersection of skills
    return (match_count / len(job_skills)) * 100  # Return match percentage

def save_results_to_file(file_name, data):
    """Saves the results to a file in the results folder."""
    with open(file_name, 'w') as file:
        file.write(data)

