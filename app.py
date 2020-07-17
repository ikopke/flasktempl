# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
from model import assigner
# -- Initialization section --
app = Flask(__name__)
# -- Routes section --

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/error', methods =['GET', 'POST'])
def error():
    return render_template("error.html")
@app.route('/riddle' , methods =['GET','POST'])
def riddle():
    user_difficulty = request.form["adversity"]
    give_riddle = assigner(user_difficulty)
    # print (request.form)
    return render_template("riddle.html", user_difficulty=user_difficulty)


@app.route('/results', methods = ['GET', 'POST'])
def results():
    return render_template("results.html")
