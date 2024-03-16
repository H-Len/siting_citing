from flask import Flask, render_template, request
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/name', methods=["POST"])
def formatName():
    fname = request.form.get('fname')
    lname = request.form.get('lname')
    return render_template('nameTemplate.html', fname=fname, lname=lname)

@app.route('/cite_style', methods=["POST"])
def styleCitation():
    style = request.form.get('options')
    fname = request.form.get('fname')
    lname = request.form.get('lname')
    title = request.form.get('title')
    date = request.form.get('date')
    if style == 'option1':
        return render_template('mlaStyle.html', fname=fname, lname=lname, title=title, date=date)
    elif style == 'option2':
        return render_template('apaStyle.html', fname=fname, lname=lname, title=title, date=date)
    elif style == 'option3':
        return render_template('chicagoStyle.html', fname=fname, lname=lname, title=title, date=date)
    elif style == 'option4':
        if len(title) >=10:
            title = f"{title[:10]}..."
        return render_template('inlineMLA.html', lname=lname, fname=fname, title =title, date=date)
    else:
        return "hmmm, we can't support invisible red ink, yet"