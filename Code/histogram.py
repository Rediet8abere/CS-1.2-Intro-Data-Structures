
def histogram(content):
    """ Takes a source_text contents of the file as a string and
        return a histogram data structure that stores each unique
        word along with the number of times the word appears in the source text."""
    # print(content)
    words = content.split()
    # list of lists
    histogram = []
    for index in range(len(words)):
        if not any(words[index] in word_count for word_count in histogram):
            histogram.append([words[index], words.count(words[index])])

    # print(histogram)
    # unique_words(histogram)
    # frequency("Fowler", histogram)

    # list of tuples
    histogram = []
    for index in range(len(words)):
        if not any(words[index] in word_count for word_count in histogram):
            histogram.append((words[index], words.count(words[index])))

    # print(histogram)

    # Dictionary
    histogram = {}
    for index in range(len(words)):
        if not any(words[index] in word_count for word_count in histogram):
            histogram[words[index]] = words.count(words[index])

    # print(histogram)

    # list of tuples of list
    histogram = []
    for index in range(len(words)):
        if not any (words.count(words[index]) in tuples for tuples in histogram):
            word_list = []
            word_list.append(words[index])
            histogram.append((words.count(words[index]), word_list))
        else:
            for tuples in histogram:
                count, word_list = tuples
                if words.count(words[index]) is count and words[index] not in word_list:
                    word_list.append(words[index])


    print(histogram)

# make it faster
def unique_words(histogram):
    """Takes a histogram argument and returns the total count
        of unique words in the histogram. For example, when given
        the histogram for The Adventures of Sherlock Holmes,
        it returns the integer 8475."""
    unique_count = 0
    for list in histogram:
        for index in range(len(list)):
            if type(list[index]) is int and list[index]== 1:
                unique_count+=1
    # print(unique_count)
    # return unique_count

# make it faster
def frequency(word, histogram):
    """Takes a word and histogram
        argument and returns the number of times that word appears
        in a text. For example, when given the word "mystery" and
        the Holmes histogram, it will return the integer 20."""
    # print(word)
    # print(histogram)
    for list in histogram:
        for index in range(len(list)):
            if type(list[index]) is str and list[index] == word:
                print(list[index])
                print(list[index+1])



if __name__ == "__main__":
    file = open("test.txt", "r")
    content = file.read()
    histogram(content)
