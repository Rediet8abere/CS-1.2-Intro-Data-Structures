import dictogram
import random
token = 'one fish two fish red fish blue fish'
token = list(token.split())
def markov_chains(token):
    """ Takes a token as an argument and creates a markov chain
        to generate a sentence.
    """
    word_dict = {}
    word_list = []
    for index in range(len(token)-1):
        if not any(token[index] in word_count for word_count in word_dict):
            word_list.append(token[index+1])
            word_dict[token[index]] = word_list
        else:
            if token[index] in word_dict.keys():
                value = word_dict.get(token[index])
                value.append(token[index+1])
        word_list = []

    for key, value in word_dict.items():
        word_dict[key] = dictogram.Dictogram(value)
    first_word = random.choice(list(word_dict.keys()))
    print("first_word", first_word)
    sentence = [first_word]
    for i in range(5):
        for key, value in word_dict.items():
            if key == first_word:
                next_word = value.sample()
                sentence.append(next_word)
                first_word = next_word
    print(sentence)
    sentence = ' '.join(sentence)
    print(sentence)
markov_chains(token)
