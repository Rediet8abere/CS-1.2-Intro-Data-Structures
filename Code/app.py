from flask import Flask
from dictionary_words import *
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    # print(random_words())
    return "random_words(10)"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))
