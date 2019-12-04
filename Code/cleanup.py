# remove punctuation and numbers
# lower letters
import re
import string
def clean_text():
    """ Input: A text file
        Process: Removes punctuation marks, text surrounded by digits and number
                and, remaning punctuation from the above cleanup.
        Output: clean text as a string
    """
    file = open("test.txt")
    content = file.read()
    file.close()
    content = content.lower()
    content = re.sub(r'[%s]' % re.escape(string.punctuation), '', content)
    content = re.sub(r'\w*\d\w*', '', content)
    content = re.sub(r'[''""...“”’‘]', '', content)
    content = re.sub(r'\n', '', content)
    return content

if __name__ == '__main__':
    text = clean_text()
    print(text)
