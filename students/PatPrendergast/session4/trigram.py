import string, random

title = "Sherlock Holmes: A SCANDAL IN BOHEMIA"
the_text = "holmes.txt"

 
def process_text_to_list(text):
    fop = open(text, 'r')
    text = fop.read()
    word_list = []
    for word in text.split(): # split words at spaces.
        # strip words of punctuation and whitespace from string module.
        word = word.strip(string.punctuation + string.whitespace) 
        word = word.lower() 
        word_list.append(word)
    return word_list


def create_trigrams(word_list):
    # example trigram: {('natural', 'selection'): ['is', 'is', 'means']}
    trigrams = {}   
    for i in range(len(word_list)-2):
        key = (word_list[i], word_list[i+1])
        if key not in  trigrams:
            value = [word_list[i+2]]
            trigrams[key] = value
        else:   
            trigrams[key].append(word_list[i+2])
    return trigrams

def rewrite_text(text):
    pass

if __name__ == '__main__':
    word_list = process_text_to_list('short_holmes.txt')
    trigrams = create_trigrams(word_list) # call the process file function
    print trigrams
    
