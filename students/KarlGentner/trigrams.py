import codecs
import string

# Open, read, and close
f = codecs.open("sherlock_small.txt")
text = f.read()
f.close()
# Make a mapping of punctuation to space using string.maketrans(from, to)
punc_to_space = string.maketrans(string.punctuation, ' '*len(string.punctuation))
# Translate text using mapping
text = text.translate(punc_to_space)
# Create a list of words from text
words = text.split()
# In a dictionary, fill keys and values with word-level trigrams
d = {}
for i in range(len(words)-2):
    key = words[i] + " " + words[i+1]
    value = words[i+2]
    if key in d:
        d[key].append(value)
    else:
        d[key] = [value]
