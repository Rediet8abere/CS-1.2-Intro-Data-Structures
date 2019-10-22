import random
import sys

def rearrange(words):
    arrange = len(words)
    while arrange > 0:
        index = random.randint(0, arrange-1)
        temp = words[index]
        words[index] = words[index - 1]
        words[index - 1] = temp
        arrange-=1
    words = ' '.join(words)
    print(words)

# find the length of the word exchange the first and last letters
def reverse(words):
    reverse = []
    for index in range(len(words)):
        word = ""
        word_len = len(words[index]) - 1
        for letterindex in range(len(words[index])):
            word += words[index][word_len]
            word_len -= 1
        reverse.append(word)
    print(' '.join(reverse))




if __name__ == "__main__":
    params = sys.argv[1:]
    words = []
    for index in range(len(params)):
        word = params[index]
        words.append(word)
    rearrange(words)
    reverse(words)
