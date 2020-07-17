from flask import request
import random 
import app




#                             Easy
a = "Where can you find cities, towns, shops, and streets but no people?"
#map
b = "I'm tall when I'm young and I'm short when I'm old. What am I?"
#candle
c = "There is a rooster sitting on top of a barn. If it laid an egg, which way would it roll?"
#rosters don't lay eggs
d = "What five letter word becomes shorter when you add two letters to it?"
#short (short+er)
e = "What is so fragile that saying its name breaks it?"
#silence 
f = "What has a bottom at the top?"
#legs
g = "What has four wheels and flies?"
#garbage truck
h = "How many months have 28 days?"
#12
i = "What's black and white and read all over?"
#newspaper
j = "What word is spelled wrong in every dictionary?"
#wrong
# 
p = "When John was six years old he hammered a nail into his favorite tree to mark his height. Ten years later at age sixteen, John returned to see how much higher the nail was. If the tree grew by five centimeters each year, how much higher would the nail be?"
# The nail would be at the same height since trees grow at their tops.
t = "Everyone has it, but no one can lose it. What is it?"
# a shadow
u = "What is it that given one, you'll have either two or none?"
# choice
v = "What English word retains the same pronunciation, even after you take away four of its five letters?"
# queue
w = "Can you write down eight eights so that they add up to one thousand?"
# 888 + 88 + 8 + 8 + 8 = 1000.
x = "When John was six years old he hammered a nail into his favorite tree to mark his height. Ten years later at age sixteen, John returned to see how much higher the nail was. If the tree grew by five centimeters each year, how much higher would the nail be?"
# The nail would be at the same height since trees grow at their tops.
y = "There was a man who was born before his father, killed his mother, and married his sister. Yet, there was nothing wrong with what he had done. Why?"
# His father was in front of him when he was born, therefore he was born before him. His mother died while giving birth to him. Finally, he grew up to be a minister and married his sister at her ceremony.

easylist = [a, b, c, d, e, f, g, h, i, j]
# mediumlist = [k, l, m, n, o, p, q, r, u, s]
# hardlist = [t, u, v, w, x, y, z, aa, ab, ac]
def riddles():
    if request.form(user_difficulty) == "Easy":
        rid = randint(0, 9)
        riddle = easylist[rid]
        return riddle
    elif request.form(user_difficulty) == "Medium":
        rid = randint(0, 9)
        riddle = mediumlist[rid]
        return riddle
    elif request.form(user_difficulty) == "Hard":
        rid = randint(0, 9)
        riddle = hardlist[rid]
        return riddle
    else:
        return "hello"