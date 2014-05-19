import codecs
def rot13(text):
    return text.encode('rot13')

if __name__ == '__main__':
    text=raw_input("Please enter a string: ")
    print rot13(text)


