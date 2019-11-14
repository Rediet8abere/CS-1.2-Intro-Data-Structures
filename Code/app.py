from flask import Flask, render_template
from dictionary_words import *
import markov
import os
token = 'TOM and JERRY traversed the Gardens, and enjoyed themselves to the utmost extent in all the variety they afforded, till day-light had long given them the hint it was time to think of home. LOGIC, as upon former occasions, was not to be found; and the CORINTHIAN and his COZ were compelled to leave Vauxhall without him.'
token = list(token.split())
app = Flask(__name__)
@app.route('/')
def tweet():
    # print(random_words())
    print("markov.markov_chains(token)", markov.markov_chains(token))
    return render_template('index.html', sentence=markov.markov_chains(token))
    # return , words=random_words(10))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))
