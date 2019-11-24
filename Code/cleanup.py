# remove punctuation and numbers
# lower letters
import re
import string

def clean_text():
    file = open("Tom_and_Jerry.txt")
    content = file.read()
    content = content.lower()
    # looks for a punctuation mark and replaces them with nothing
    content = re.sub(r'[%s]' % re.escape(string.punctuation), '', content)
    content = re.sub(r'\w*\d\w*', '', content)
    file.close()
    return content


if __name__ == '__main__':
    word_list = clean_text()
    print(word_list)
