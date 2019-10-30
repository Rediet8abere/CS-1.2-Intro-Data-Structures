# count slow
import random
import numpy as np
def histogram(content):
    """ Takes a source_text contents of the file as a string and
        return a histogram data structure that stores each unique
        word along with the number of times the word appears in the source text."""
    words = content.split()
    # list of lists
    histogram_list = []
    for index in range(len(words)):
        if not any(words[index] in word_count for word_count in histogram_list):
            histogram_list.append([words[index], words.count(words[index])])

    # list of tuples
    histogram_tuples = []
    for index in range(len(words)):
        if not any(words[index] in word_count for word_count in histogram_tuples):
            histogram_tuples.append((words[index], words.count(words[index])))

    # Dictionary
    histogram_dic = {}
    for index in range(len(words)):
        if not any(words[index] in word_count for word_count in histogram_dic):
            histogram_dic[words[index]] = 1
        else:
            histogram_dic[words[index]]+= 1
    # unique_words(histogram_dic)
    # frequency("fish", histogram_dic)
    words_chose = []
    for i in range(20):
        words_chose.append(sampling(histogram_dic))
    print(words_chose)

    # list of count
    histogram_count = []
    for index in range(len(words)):
        if not any (words.count(words[index]) in tuples for tuples in histogram_count):
            word_list = []
            word_list.append(words[index])
            histogram_count.append((words.count(words[index]), word_list))
        else:
            for tuples in histogram_count:
                count, word_list = tuples
                if words.count(words[index]) is count and words[index] not in word_list:
                    word_list.append(words[index])

def unique_words(histogram):
    """Takes a histogram argument and returns the total count
        of unique words in the histogram. For example, when given
        the histogram for The Adventures of Sherlock Holmes,
        it returns the integer 8475."""
    print(f"unique words {len(histogram)}")
    return len(histogram)


def frequency(word, histogram):
    """Takes a word and histogram
        argument and returns the number of times that word appears
        in a text. For example, when given the word "mystery" and
        the Holmes histogram, it will return the integer 20."""
    print(histogram)
    if histogram[word]:
        print(f"frequency of {word} is {histogram[word]}")
        return histogram[word]

def sampling(histogram):
    """The first weighting we'll apply is a frequency weighting:
     words which appear more frequently in the original text
     should be more likely to be selected by our sampling program."""
    hist_keys = list(histogram.keys())
    total = sum(list(histogram.values()))
    p = []
    for value in list(histogram.values()):
        prob_dis = value/total
        p.append(prob_dis)

    words = []
    dict = {}
    for prob, word in zip(p, hist_keys):
        dict['word'] = word
        dict['chance'] = prob
        words.append(dict.copy())
    print(words)

    rand = random.uniform(0, 1)
    print(rand)
    chosen_word = []
    for i in range(len(words)):
        word_choice=words[i]
        if rand < word_choice['chance']:
            chosen_word.append(word_choice['word'])
            return word_choice['word']
        rand-=word_choice['chance']
    print(chosen_word)

    # words_drawn = []
    # for i in range(10):
    #     draw = np.random.choice(list(histogram.keys()), 1, p=p)
    #     words_drawn.append(draw[0])
    # print(words_drawn)


if __name__ == "__main__":
    file = open("test.txt", "r")
    content = file.read()
    histogram(content)
