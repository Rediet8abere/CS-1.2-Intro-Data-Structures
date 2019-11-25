from flask import Flask, render_template
import markov
import os


app = Flask(__name__)

@app.route('/')
def tweet():
    sentence = markov.Markov()
    sentence.dict_list()
    sentence.dictogram_dictlist()
    sentence = sentence.generate()
    return render_template('index.html', sentence=sentence)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))
