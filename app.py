"""Using speed model to run the app"""
from speedy.speed import speedTry
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def speed():
    #TODO(mwala) add a web ui for the service in the templates dir
    return render_template('index.html')

@app.route("/speed", methods=['POST'])
def doTest():
    speedTry()
    return "Speed"
