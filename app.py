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