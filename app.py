from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/time')
def timeNow():
    currentTime = datetime.datetime.now()
    return render_template('formatTime.html', currentTime=currentTime)

@app.route('/name')
def formatName():
    return render_template('nameTemplate.html', fname='Zev', lname='Cohen')