import random
import sys

def rearrange(word_1, word_2, word_3, word_4):
    word_list = [word_1, word_2, word_3, word_4]

    arrange = len(word_list)

    while arrange > 0:
        for index in range(arrange-1):
            if word_list[index] > word_list[index + 1]:
                temp = word_list[index]
                word_list[index] = word_list[index + 1]
                word_list[index + 1] = temp
                print(word_list[index], word_list[index + 1])
        arrange-=1
    print(word_list)



if __name__ == "__main__":
    params = sys.argv[1:]
    word_1 = params[0]
    word_2 = params[1]
    word_3 = params[2]
    word_4 = params[3]

    rearrange(word_1, word_2, word_3, word_4)
