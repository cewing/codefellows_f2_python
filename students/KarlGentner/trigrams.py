import codecs
import string

# Open, read, and close
f = codecs.open("sherlock.txt")
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


# Create altered text starting point of three words
start = d.popitem()
altText = "{key} {value}".format(key=start[0].capitalize(), value=start[1][0])
words = altText.split()
nextKey = words[len(words)-2] + " " + words[len(words)-1]
# Fill the rest of altText
while nextKey in d:
    # Pop one value if key has more than 1 in value list
    if len(d.get(nextKey)) > 1:
        nextWord = d.get(nextKey).pop(1)
    else:
        nextWord = d.pop(nextKey)[0]
    altText += " " + nextWord + " "
    words = altText.split()
    nextKey = words[len(words)-2] + " " + words[len(words)-1]
# Add "periods" before capitalized words
words = altText.split()
altText = words.pop(0)
for i in range(len(words)-1):
    altText += " " + words[i]
    if not words[i+1].islower():
        altText += "."