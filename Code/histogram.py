
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
    unique_words(histogram)

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

    # counts_list = [(1, ['one', 'two', 'red', 'blue']), (4, ['fish'])]
    # histogram = []
    # for index in range(len(words)):
    #     if not any(words[index] in word_count for word_count in histogram):
    #         if words.count(words[index])
    #         histogram.append((words.count(words[index]), words[index]))
    #
    # print(histogram)

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
    print(unique_count)



if __name__ == "__main__":
    file = open("test.txt", "r")
    content = file.read()
    histogram(content)
