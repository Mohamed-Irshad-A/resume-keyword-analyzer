from flask import Flask, render_template, request
app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    if request.method=="POST":
        resume_text=request.form['resume']
        job_text=request.form['job']
        return render_template('result.html')
    return render_template('index.html')

if __name__=='__main__':
    app.run(debug=True)