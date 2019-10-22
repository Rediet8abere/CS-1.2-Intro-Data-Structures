import random
import sys

def rearrange(word_1, word_2, word_3, word_4):
    word_list = [word_1, word_2, word_3, word_4]

    arrange = len(word_list)-1

    while arrange > 0:
        for i in range(arrange-1):
            index = random.randint(0, arrange)
            if index < arrange:
                temp = word_list[index]
                word_list[index] = word_list[index + 1]
                word_list[index + 1] = temp
            else:
                temp = word_list[index]
                word_list[index] = word_list[index - index]
                word_list[index - index] = temp
        arrange-=1
    words = ' '.join(word_list)
    print(words)

if __name__ == "__main__":
    params = sys.argv[1:]
    word_1 = params[0]
    word_2 = params[1]
    word_3 = params[2]
    word_4 = params[3]

    rearrange(word_1, word_2, word_3, word_4)
