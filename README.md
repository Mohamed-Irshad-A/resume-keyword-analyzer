# Resume Keyword Analyzer

A simple web app that compares a resume with a job description using NLP to calculate how well the keywords match.

## Features

- Extracts keywords from resume and JD
- Calculates matching %
- Highlights matched words

## Tech Stack

- Flask
- Python
- spaCy

## Screenshot

### Home Page
![Home](screenshots/home.png)

### Result Page
![Result](screenshots/result.png)

## Run Locally

```bash
git clone https://github.com/Mohamed-Irshad-A/resume-keyword-analyzer.git
cd resume-keyword-analyzer
pip install -r requirements.txt
python -m spacy download en_core_web_sm
python app.py 