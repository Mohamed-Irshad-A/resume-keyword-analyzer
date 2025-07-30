from flask import Flask, render_template, request
import spacy

app=Flask(__name__)
nlp = spacy.load('en_core_web_sm')

def extract_keywords(text):
    doc=nlp(text)
    return set([token.lemma_.lower() for token in doc if token.pos_ in ['NOUN', 'PROPN', 'VERB'] and not token.is_stop])

@app.route('/',methods=['GET','POST'])
def index():
    if request.method=="POST":
        resume_text=request.form['resume']
        job_text=request.form['job']

        resume_keywords=extract_keywords(resume_text)
        job_keywords=extract_keywords(job_text)

        matched=resume_keywords & job_keywords
        match_percent=(len(matched)/len(job_keywords))*100 if job_keywords else 0

        return render_template('result.html', percent=round(match_percent,2),matched=matched)

    return render_template('index.html')

if __name__=='__main__':
    app.run(debug=True)