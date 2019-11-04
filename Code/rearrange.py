import random
import sys

def rearrange(words):
    """Rearranges words randomly from words list. """
    words = words.copy()
    arrange = random.randint(1, len(words))
    while arrange > 0:
        max = len(words) - 2
        index = random.randint(0, max)
        temp = words[index]
        words[index] = words[abs(index + 1)]
        words[abs(index + 1)] = temp
        arrange-=1
    words = ' '.join(words)
    print(words)

def reverse(words):
    """Revese words from the words list. """
    reverse = []
    for index in range(len(words)):
        word = ""
        word_len = len(words[index]) - 1
        for letterindex in range(len(words[index])):
            word += words[index][word_len]
            word_len -= 1
        reverse.append(word)
    print(' '.join(reverse))

def  anagram(words):
    """shuffles the letters in a word and creates a different word with meaning."""
    words_in =  words.copy()
    words_in = ' '.join(words_in)

    # remove space
    # make sure to generate the same len of words
    words_in = words_in.replace(" ", "")
    words_in = words_in.lower()
    print(words_in)
    anagram = ""
    rand_index = random.sample(range(len(words_in)), len(words_in))
    print("rand", rand_index)
    for rand in rand_index:
        print(rand, words_in[rand])
        anagram+=words_in[rand]
    print(anagram)
    # file = open("/usr/share/dict/words")
    file = open("test.txt", 'r')
    content = file.readlines()
    file.close()
    for word in content:
        word = word.strip('\n')
        print(word)

        # if word == anagram:
        #     print("hello")
        #     print(word, anagram)



    # print(content)
    # while



if __name__ == "__main__":
    params = sys.argv[1:]
    if len(params) <1:
        print("please add atleast 2 words next to file name :)")
    else:
        words = []
        for index in range(len(params)):
            word = params[index]
            words.append(word)
        # rearrange(words)
        # reverse(words)
        anagram(words)
