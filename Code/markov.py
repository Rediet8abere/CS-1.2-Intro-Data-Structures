import dictogram
import random

import cleanup
import tokenize

text = cleanup.clean_text()
token = tokenize.token(text)

class markov(object):
    def __init__(self, token):
        self.token = token
        self.word_dict = {}

    def dict_list(self):
        """ Takes in token as a list to create a dictionary of types and
        words that follows the types
        """
        word_list = []
        for index in range(len(self.token)-1):
            if self.token[index] not in self.word_dict:
                word_list.append(self.token[index+1])  # Appends words that follow the types
                self.word_dict[self.token[index]] = word_list  # Create a dictionary based on types and it's word list
            else:
                if self.token[index] in self.word_dict.keys():
                    value = self.word_dict.get(self.token[index]) # gets the list if the type already exists
                    value.append(self.token[index+1]) # and append the new word to the list
            word_list = []

    def dictogram_dictlist(self):
        """ Converts the list in word_dict to dictionary
        by calling Dictogram on the values.
        """
        for key, value in self.word_dict.items():
                self.word_dict[key] = dictogram.Dictogram(value)

    def generate(self):
        """ Generates a sentence based on sampled
        random word choice
        """
        first_word = random.choice(list(self.word_dict.keys())) # first word for our sentence
        first_word = first_word.capitalize()
        sentence = [first_word]
        for i in range(10):
            val = random.choice(list(self.word_dict.values()))
            next_word = val.sample()
            sentence.append(next_word)
        sentence = ' '.join(sentence)
        return sentence + "."

if __name__ == '__main__':
    markov = markov(token)
    markov.dict_list()
    markov.dictogram_dictlist()
    print(markov.generate())
