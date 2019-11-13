from flask import Flask, render_template
from dictionary_words import *
import markov
import os
token = 'To Sherlock Holmes she is always _the_ woman. I have seldom heard him mention her under any other name. In his eyes she eclipses and predominates the whole of her sex. It was not that he felt any emotion akin to love for Irene Adler. All emotions, and that one particularly, were abhorrent to his cold, precise, but admirably balanced mind. He was, I take it, the most perfect reasoning and observing machine that the world has seen; but, as a lover, he would have placed himself in a false position.'
token = list(token.split())
# virtulal enviroment
app = Flask(__name__)
# I think you should create a histogram with a source_text here instead of using the histogram of random_words
@app.route('/')
def tweet():
    # print(random_words())
    print("markov.markov_chains(token)", markov.markov_chains(token))
    return render_template('index.html', sentence=markov.markov_chains(token))
    # return , words=random_words(10))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))
