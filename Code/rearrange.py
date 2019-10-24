import random
import sys
# same
# ranint(0, len(list)-1)
# randrange(len(list))

# write test function
# finish up anagram
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
    """shuffles the letters in a word and creates a different word with meaning.
        The longest word in english which is: 'pneumonoultramicroscopicsilicovolcanoconiosis'
         is used to consider max length of a word. """
    # randomly consturct a word check if that word exists in the dictionary if does append to sentence
    max_len = len("pneumonoultramicroscopicsilicovolcanoconiosis")
    print(max_len)
    word = ""
    for index in range(len(words)):
        for letterindex in range(len(words[index])):
            word += words[index][letterindex]
    print(word)
    print(len(word))
    len_word = len(word)-1
    random_len = random.randint(0, len_word)
    random_word_list = []
    for i in range(random_len):
        rand_word = ""
        random_len = random.randint(0, len_word)
        for letterindex in range(random_len):
            print("letter", word[letterindex])
            rand_word += word[random.randint(0, len_word)]
            # randomly decide the length of a word
            # make sure to store the ws
            # randomly choose letters to make up a word
            print(letterindex)
        random_word_list.append(rand_word)
        print("random word", rand_word)
    print("expecting list with random words", random_word_list)


if __name__ == "__main__":
    params = sys.argv[1:]
    words = []
    for index in range(len(params)):
        word = params[index]
        words.append(word)
    rearrange(words)
    # reverse(words)
    # anagram(words)
