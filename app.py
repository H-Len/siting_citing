from flask import Flask, render_template, request
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/time')
def timeNow():
    currentTime = datetime.datetime.now()
    return render_template('formatTime.html', currentTime=currentTime)

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
        return render_template('inlineMLA.html', lname=lname, fname=fname, title =title, date=date)
    else:
        return "hmmm, we can't support invisible red ink, yet"

# Formats:
# MLA:
    # Author's Last name, First name. "Title of Source." Title of Container, Other contributors, Version, Numbers, Publisher, Publication Date, Location.
# APA:
    # A basic reference list entry for a journal article in APA must include:
    # Author or authors. ...
    # Year of publication of the article (in round brackets).
    # Article title.
    # Journal title (in italics).
    # Volume of journal (in italics).
    # Issue number of journal in round brackets (no italics).
    # Page range of article.
    # DOI or URL.
# Chicago:
    # for a book, this is like MLA
    # Chicago author-date format	
    #   Author last name, first name. Year. Book Title: Subtitle. Place of publication: Publisher. Format.
    # Chicago reference entry	
    #   Murdoch, Iris. 2008. The Sea, the Sea. London: Vintage. Kindle.