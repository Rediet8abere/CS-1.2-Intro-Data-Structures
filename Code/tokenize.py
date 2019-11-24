def token():
    "Read words file"
    file = open("Tom_and_Jerry.txt")
    content = file.read()
    # content = "Hello World, How are you doing. I hope you have a blessed day and night!"
    word_token = list(content.split())
    file.close()
    return word_token

if __name__ == "__main__":
    word_list = token()
    print(word_list)
    print(type(word_list))
