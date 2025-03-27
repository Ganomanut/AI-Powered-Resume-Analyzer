from flask import Flask, render_template, request, jsonify, redirect, url_for
import os
from PyPDF2 import PdfReader
from docx import Document
import re

app = Flask(__name__)

# Upload folder configuration
UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


# Function to extract text from PDF
def extract_text_from_pdf(file_path):
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text


# Function to extract text from DOCX
def extract_text_from_docx(file_path):
    doc = Document(file_path)
    text = ""
    for paragraph in doc.paragraphs:
        text += paragraph.text + "\n"
    return text


# Function to determine file type and extract text
def extract_resume_data(file_path):
    if file_path.endswith(".pdf"):
        return extract_text_from_pdf(file_path)
    elif file_path.endswith(".docx"):
        return extract_text_from_docx(file_path)
    else:
        return "Unsupported file format. Please upload a PDF or DOCX file."


# Function to predict specialization based on keywords
def predict_specialization(resume_text):
    keywords = {
        "Data Science": [
            "machine learning",
            "data analysis",
            "python",
            "pandas",
            "numpy",
        ],
        "Web Development": ["html", "css", "javascript", "react", "angular", "node.js"],
        "Software Engineering": [
            "java",
            "c++",
            "c#",
            "software development",
            "system design",
        ],
        "Digital Marketing": ["seo", "social media", "content marketing", "google ads"],
        "UI/UX Design": [
            "user interface",
            "user experience",
            "wireframes",
            "prototyping",
        ],
        "Network security": ['troubleshooting','configuration',]
    }

    for specialization, words in keywords.items():
        for word in words:
            if re.search(rf"\b{word}\b", resume_text, re.IGNORECASE):
                return specialization
    return "Unknown Specialization"


# Home route
@app.route("/")
def resumeupload():
    return render_template("resumeupload.html")
@app.route('/')
def job_matching():
    return render_template('scoring&ranking.html')


# Upload route
@app.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return jsonify({"error": "No file part in the request."})
    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "No file selected."})
    if file:
        file_path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(file_path)
        resume_text = extract_resume_data(file_path)
        specialization = predict_specialization(resume_text)
        return jsonify(
            {
                "message": "File uploaded successfully!",
                "resume_text": resume_text,
                "specialization": specialization,
            }
        )

@app.route('/candidatescreening')
def candidate_screening():
    return render_template('Job__matching.html')

@app.route('/jobrecommendations')
def job_recommendations():
    return render_template('AT&HRtrack.html')


if __name__ == "__main__":
    app.run(debug=True)
