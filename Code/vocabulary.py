from PyDictionary import PyDictionary
import dictionary_words

class Vocabulary(object):
    """Flash a word, player has to guess the
       definition, then is shown the definition.
    """
    result = None
    generate = True
    while generate:
        word = dictionary_words.random_words()
        definition = PyDictionary()
        result = definition.meaning(word)
        if result:
            user = input(f"Wanna guess the definition of {word}? ")
            for key, value in result.items():
                print(key, ": ", value[0])
            generate = False

if __name__ == "__main__":
    flash = Vocabulary()
