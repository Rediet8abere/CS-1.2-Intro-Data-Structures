import random
import sys

def read_words():
    "Read words file"
    # file = open("/usr/share/dict/words")
    file = open("test.txt")
    content = file.readlines()
    file.close()
    return content
# lines = []
# for line in all_lines
#   lines.append(line.strip())
# lines = [line.strip() for line in all_lines]
def random_words(word_num=1):
    "Generate sentence constructed by random words"
    words = read_words()
    print(words)
    print(word_num)
    random_words = []
    for i in range(int(word_num)):
        random_index = random.randint(0, len(words)-1)
        random_words.append(words[random_index].strip('\n'))
    sentence = ' '.join(random_words)

    print(sentence)
    return sentence


if __name__ == "__main__":
    # open the file here to open it only one time
    params = sys.argv[1:]
    if params:
        word_num = params[0]
        random_words(word_num)
    else:
        print("Pass in a number in the command line")
        random_words()
