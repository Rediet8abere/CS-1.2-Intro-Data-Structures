import dictogram
import random
import words_list
import cleanup

# Comedy Central

class Markov(object):
    """ Generates sentence based on word distribution
    """
    def __init__(self):
        self.text = cleanup.clean_text()
        self.token = words_list.token(self.text)
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
            # if self.word_dict.get(key) is not None:
            # print(self.word_dict.get(key))
            self.word_dict[key] = dictogram.Dictogram(value)

    def generate(self, count=15):
        """ Generates a sentence based on sampled
        random word choice
        """
        first_word = random.choice(list(self.word_dict.keys())) # first word for our sentence
        # first_word = first_word.capitalize()
        sentence = []
        print("first_word", first_word)
        # print("self.word_dict", self.word_dict)
        for i in range(count):
            # print("self.word_dict[first_word]", self.word_dict[first_word])
            second_word = self.word_dict[first_word]
            # print("second_word", second_word)
            next_word = second_word.sample()
            first_word = next_word
            sentence.append(next_word)
        sentence = ' '.join(sentence)
        return sentence + "."

if __name__ == '__main__':
    markov = Markov()
    markov.dict_list()
    markov.dictogram_dictlist()
    print(markov.generate())
