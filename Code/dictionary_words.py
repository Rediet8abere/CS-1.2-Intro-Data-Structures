import random
import sys

def read_words():
    "Read words file"
    words = open("/usr/share/dict/words")
    content = words.readlines()
    return content

def random_words(word_num):
    "Generate sentence constructed by random words"
    words = read_words()
    random_words = []
    for i in range(int(word_num)):
        random_index = random.randint(0, len(words))
        random_words.append(words[random_index].strip('\n'))
    sentence = ' '.join(random_words)
    print(sentence)


if __name__ == "__main__":
    params = sys.argv[1:]
    word_num = params[0]
    random_words(word_num)
