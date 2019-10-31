from flask import Flask
from dictionary_words import *
app = Flask(__name__)

@app.route('/')
def hello_world():
    # print(random_words())
    return random_words(10)
