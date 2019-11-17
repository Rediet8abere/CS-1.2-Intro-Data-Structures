import dictogram
import random
# token = 'one fish two fish red fish blue fish'
source_text = '“Seven!” I answered. “Then, how do you know?”'
source_text = list(source_text.split())
def markov_chains(token):
    """ Takes a token as an argument and creates a markov chain
        to generate a sentence.
    """
    word_dict = {}
    word_list = []
    # creates a Dictionary of list
    for index in range(len(token)-1):
        # loop through the list to check if the
        print(token)
        if not any(token[index] in word_count for word_count in word_dict):
            word_list.append(token[index+1])
            word_dict[token[index]] = word_list
        else:
            if token[index] in word_dict.keys():
                value = word_dict.get(token[index])
                value.append(token[index+1])
        word_list = []
    # calls dictogram on the list inside the Dictionary to change it to a Dictionary
    capital_words = []
    ending_words = []
    for key, value in word_dict.items():
        word_dict[key] = dictogram.Dictogram(value)
        for letter in key:
            if letter.isupper():
                capital_words.append(key)
        for letter in key:
            if letter == '.':
                ending_words.append(key)
            if letter == '!':
                ending_words.append(key)
            if letter == '?':
                ending_words.append(key)
    print("ending_words", ending_words)
    print("capital_words", capital_words)
    first_word = random.choice(capital_words)
    print("first_word", first_word)
    sentence = [first_word]
    # generate a list of words based on the words weight
    for i in range(5):
        for key, value in word_dict.items():
            if key == first_word:
                next_word = value.sample()
                sentence.append(next_word)
                first_word = next_word
    sentence.append(random.choice(ending_words))

    print(sentence)
    sentence = ' '.join(sentence)
    print(sentence)
    return sentence
if __name__ == '__main__':
    sentence = markov_chains(source_text)
