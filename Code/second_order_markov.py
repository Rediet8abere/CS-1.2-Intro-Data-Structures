import dictogram
import random
import words_list
import cleanup


class Markov(object):
    """ Generates sentence based on word distribution
    """
    def __init__(self):
        self.text = cleanup.clean_text()
        self.token = words_list.token(self.text)
        self.word_dict = {}

    def two_words(self):
        words = []
        print(self.text)
        for index in range(len(self.token)-1):
            words.append((self.token[index], self.token[index+1]))
        #
        word_list = []
        for index in range(len(words)-1):
            if words[index] not in self.word_dict:
                word_list.append(self.token[index+2])  # Appends words that follow the types
                self.word_dict[words[index]] = word_list  # Create a dictionary based on types and it's word list
            else:
                if words[index] in self.word_dict.keys():
                    value = self.word_dict.get(self.token[index]) # gets the list if the type already exists
                    value.append(self.token[index+2]) # and append the new word to the list
            word_list = []

        print()
        # print("self.word_dict", self.word_dict)

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
        # print("self.word_dict", self.word_dict)

    def dictogram_dictlist(self):
        """ Converts the list in word_dict to dictionary
        by calling Dictogram on the values.
        """
        for key, value in self.word_dict.items():
            self.word_dict[key] = dictogram.Dictogram(value)
        print("self.word_dict", self.word_dict)

    def generate(self):
        """ Generates a sentence based on sampled
        random word choice
        """
        first_word = random.choice(list(self.word_dict.keys())) # first word for our sentence
        first_word = first_word[random.randint(0, 1)].capitalize()
        sentence = [first_word]
        print("self.token", self.token)
        print(len(self.token))
        print("values", list(self.word_dict.values()))
        for i in range(len(self.token)-2):
            val = list(self.word_dict.values())[i]
            print(len(val))
            print("val", val)
            next_word = val.sample()
            sentence.append(next_word)
        sentence = ' '.join(sentence)
        return sentence + "."

if __name__ == '__main__':
    markov = Markov()
    markov.two_words()
    # markov.dict_list()
    markov.dictogram_dictlist()
    print(markov.generate())
