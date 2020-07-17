# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
import model
import random
# -- Initialization section --
app = Flask(__name__)
# -- Routes section --
#                               EASY RIDDLES
a = "Where can you find cities, towns, shops, and streets but no people?"
A = "map"

b = "I'm tall when I'm young and I'm short when I'm old. What am I?"
B = "candle"

c = "There is a rooster sitting on top of a barn. If it laid an egg, which way would it roll?"
C = "rosters don't lay eggs"

d = "What five letter word becomes shorter when you add two letters to it?"
D = "short (short+er)"

e = "What is so fragile that saying its name breaks it?"
E = "silence" 

f = "What has a bottom at the top?"
F = "legs"

g = "What has four wheels and flies?"
G = "garbage truck"

h = "How many months have 28 days?"
H = "12"

i = "What's black and white and read all over?"
I = "newspaper"

j = "What word is spelled wrong in every dictionary?"
J = "wrong"

#                                           Medium
p = "When John was six years old he hammered a nail into his favorite tree to mark his height. Ten years later at age sixteen, John returned to see how much higher the nail was. If the tree grew by five centimeters each year, how much higher would the nail be?"
# The nail would be at the same height since trees grow at their tops.
#                                HARD RIDDLES
t = "Everyone has it, but no one can lose it. What is it?"
T = "a shadow"

u = "What is it that given one, you'll have either two or none?"
U = "choice"

v = "What English word retains the same pronunciation, even after you take away four of its five letters?"
V = "queue"

w = "Can you write down eight eights so that they add up to one thousand?"
W = "888 + 88 + 8 + 8 + 8 = 1000."

x = "When John was six years old he hammered a nail into his favorite tree to mark his height. Ten years later at age sixteen, John returned to see how much higher the nail was. If the tree grew by five centimeters each year, how much higher would the nail be?"
X = "The nail would be at the same height since trees grow at their tops."

y = "There was a man who was born before his father, killed his mother, and married his sister. Yet, there was nothing wrong with what he had done. Why?"
Y = "His father was in front of him when he was born, therefore he was born before him. His mother died while giving birth to him. Finally, he grew up to be a minister and married his sister at her ceremony."

# z = 
# Z = 

aa ="Forward I'm heavy, backward I'm not. What am I?"
Aa = "ton"

ab = "A man has a bee in his hand. What's in his eye?"
Ab = "beauty"

ac = "We are all very little creatures; all of us have different features. One of us in glass is set; One of us you'll find in jet. Another you may see in tin, And a fourth is boxed within. If the fifth you should pursue, It can never fly from you. What are we?"
Ac = "Vowels"

easylist = [a, b, c, d, e, f, g, h, i, j]
easyanswers = [A, B, C, D, E, F, H, I, J]
# mediumlist = [k, l, m, n, o, p, q, r, u, s]
# mediumanswer = [K, L, M, N, O, P, Q, R, U, S]
hardlist = [t, u, v, w, x, y, aa, ab, ac]
hardanswer = [T, U, V, X, X, Y, Aa, Ab, Ac]
# print(easylist[3])
def assigner(difficulty):
    if difficulty == "Easy":
        rid = random.randint(0, 9)
        riddler = easylist[rid]

        return riddler
    # elif difficulty == "Medium":
    #     rid = random.randint(0, 9)
    #     riddler = mediumlist[rid]
    #     return riddler
    elif difficulty == "Hard":
        rid = random.randint(0, 9)
        riddler = hardlist[rid]
        return riddler
#     else:
#         return "ERROR"
def answers(rid):
    if difficulty == "Easy":
        answer = easyanswer[rid]
        return answer
    # elif difficulty == "Medium":
        # riddler = mediumlist[rid]
        # return riddler
    elif difficulty == "Hard":
        rid = random.randint(0, 9)
        riddler = hardlist[rid]
        return riddler
#     else:
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
    return render_template("riddle.html", user_difficulty=user_difficulty, riddler = give_riddle)


@app.route('/results', methods = ['GET', 'POST'])
def results():
    give_answer = answers(rid)
    return render_template("results.html", give_answer = answer)
