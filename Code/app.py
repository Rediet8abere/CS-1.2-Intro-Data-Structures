from flask import Flask, render_template
from dictionary_words import *
import os
# virtulal enviroment
app = Flask(__name__)
# I think you should create a histogram with a source_text here instead of using the histogram of random_words
@app.route('/')
def hello_world():
    # print(random_words())
    return render_template('index.html', sentence=random_words(10))
    # return , words=random_words(10))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))
