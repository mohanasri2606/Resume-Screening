import os
from resume_parser import extract_text_from_pdf, extract_skills
from job_matcher import load_job_description, calculate_match_percentage, save_results_to_file
import matplotlib.pyplot as plt

# Define paths
resume_folder = "data/resumes/"
job_folder = "data/job_descriptions/"
results_folder = "results/"

# Predefined Skill Set for Full Stack Developer
job_skills = ["Python", "SQL", "JavaScript", "Node.js", "Django"]

# Function to process resumes and calculate match percentage
def process_resumes():
    results = []

    # Loop through all resumes in the folder
    for resume_file in os.listdir(resume_folder):
        if resume_file.endswith(".pdf"):
            resume_path = os.path.join(resume_folder, resume_file)
            resume_text = extract_text_from_pdf(resume_path)  # Extract text from resume

            # Extract skills from the resume
            resume_skills = extract_skills(resume_text, job_skills)

            # Load the job description (for Full Stack Developer)
            job_file = os.path.join(job_folder, "full_stack_developer.txt")
            job_description = load_job_description(job_file)

            # Extract skills from the job description
            job_skills_from_desc = extract_skills(job_description, job_skills)

            # Calculate the match percentage
            match_percentage = calculate_match_percentage(resume_skills, job_skills_from_desc)

            # Store the result as a tuple of resume name and match percentage
            results.append((resume_file, match_percentage))

            # Prepare the result text
            result_text = f"Resume: {resume_file}\nSkills: {', '.join(resume_skills)}\nMatch Percentage: {match_percentage}%\n\n"
            save_results_to_file(os.path.join(results_folder, f"{resume_file}_result.txt"), result_text)

            # Optionally, print the result
            print(result_text)

    # Sort the results by match percentage in descending order
    sorted_results = sorted(results, key=lambda x: x[1], reverse=True)

    return sorted_results

# Main function to start the process
if __name__ == "__main__":
    # Ensure the 'results' folder exists
    os.makedirs(results_folder, exist_ok=True)
    
    # Process the resumes and get sorted results
    sorted_results = process_resumes()

    # Print the sorted results
    print("\nSorted Results (Descending Order of Match Percentage):")
    for resume, match_percentage in sorted_results:
        print(f"{resume}: {match_percentage}%")

    # Generate a chart (bar plot) for sorted resume categories
    resumes = [resume for resume, _ in sorted_results]
    match_percentages = [match_percentage for _, match_percentage in sorted_results]

    plt.barh(resumes, match_percentages, color='skyblue')
    plt.title("Resume Match Percentages")
    plt.xlabel("Match Percentage")
    plt.ylabel("Resumes")
    plt.tight_layout()
    plt.show()
