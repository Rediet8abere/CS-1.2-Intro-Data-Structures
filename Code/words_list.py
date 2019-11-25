# import cleanup

def token(text):
    """ Input: string that is clean text
        Process: converts string to list of words
        Output: List of words
    """
    word_list = list(text.split())
    return word_list

if __name__ == "__main__":
    # text = cleanup.clean_text()
    token(text)
    # word_list = token(text)
    # print(word_list)
