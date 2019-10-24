
def histogram(content):
    """ A histogram() function which takes a source_text argument
        (can be either a filename or the contents of the file as a string,
        your choice) and return a histogram data structure that stores each
        unique word along with the number of times the word appears in the source text."""
    print(content)
    words = content.split()
    # list of lists
    histogram = []
    for index in range(len(words)):
        if not any(words[index] in word_count for word_count in histogram):
            histogram.append([words[index], words.count(words[index])])

    print(histogram)

    # list of tuples
    histogram = []
    for index in range(len(words)):
        if not any(words[index] in word_count for word_count in histogram):
            histogram.append((words[index], words.count(words[index])))

    print(histogram)

    # Dictionary
    histogram = {}
    for index in range(len(words)):
        if not any(words[index] in word_count for word_count in histogram):
            histogram[words[index]] = words.count(words[index])

    print(histogram)

    



if __name__ == "__main__":
    file = open("test.txt", "r")
    content = file.read()
    histogram(content)
