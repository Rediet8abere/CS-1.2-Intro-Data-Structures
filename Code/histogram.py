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
    print("pritting frequency", frequency("f", histogram_dic))
    # sampling(histogram_dic)
    # words_chose = []
    # for i in range(10):
    #     words_chose.append(sampling(histogram_dic))
    # print(words_chose)

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
        in a text. For example, when given the word "fish" and
        the Holmes histogram, it will return the integer 4."""
    print(histogram)
    # freq = histogram.get(word)
    # if freq:
    #     print(f"frequency of {word} is {freq}")
    #     return freq
    # return 0
    if histogram[word]:
        return histogram[word]

def sampling(histogram):
    """The first weighting we'll apply is a frequency weighting:
     words which appear more frequently in the original text
     should be more likely to be selected by our sampling program."""
    hist_keys = list(histogram.keys())
    hist_values = list(histogram.values())
    token = sum(list(histogram.values()))

    rand_int = random.randint(1, token)

    for i in range(len(histogram)):
        word_dist = hist_values[i]
        if rand_int <= word_dist:
            return hist_keys[i]
        rand_int-=word_dist



if __name__ == "__main__":
    file = open("test.txt", "r")
    content = file.read()
    histogram(content)
