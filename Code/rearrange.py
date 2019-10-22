import random
import sys

def rearrange(words):
    arrange = len(words)
    while arrange > 0:
        for i in range(arrange):
            index = random.randint(0, arrange)
            if index < arrange:
                temp = words[index]
                words[index] = words[index - 1]
                words[index - 1] = temp
        arrange-=1
    words = ' '.join(words)
    print(words)

if __name__ == "__main__":
    params = sys.argv[1:]
    words = []
    for index in range(len(params)):
        word = params[index]
        words.append(word)
    rearrange(words)
