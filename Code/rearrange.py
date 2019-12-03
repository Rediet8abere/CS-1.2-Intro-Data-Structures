import random
import sys
import dictionary_words

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
    return words

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
    return ' '.join(reverse)

def anagram(words):
    # content = dictionary_words.read_words()
    content = ["apple", "banana", "cat", "dog", "life", "yo"]
    low = 0
    high = len(content) - 1
    mid = (low + high)//2
    while low <= high:
        print(low)
        if "life" == content[mid]:
            return True
        elif "life" <= content[mid]:
            print("elif", content[mid])
            high = mid - 1
        elif "life" > content[mid]:
            print("low before", low)
            print("else", content[mid])
            low = mid - 1
            print("low", low)
        print("mid", mid)
    return


if __name__ == "__main__":
    params = sys.argv[1:]
    if len(params) < 1:
        print("please add atleast 2 words next to file name :)")
    else:
        words = []
        for index in range(len(params)):
            word = params[index]
            words.append(word)
        print("rearranged word: ", rearrange(words))
        print("words reversed: ", reverse(words))
        anagram(words)
