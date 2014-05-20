import codecs
import random

f = codecs.open("sherlock.txt", 'r')
story = f.read().split()
f.close()

word_dict = {}
new_story = []
for i in range(len(story)-3):
    word1 = story[i]
    word2 = story[i+1]
    word3 = story[i+2]
    word_dict.setdefault(word1 + ' ' + word2, []).append(word3)

def get_seed():
    seed_words = word_dict.keys()
    rnd_value = int(random.random() * len(seed_words))
    seed_phrase = seed_words[rnd_value].split()
    word0 = seed_phrase[0]
    word1 = seed_phrase[1]
    new_story.append(word0)
    new_story.append(word1)

for i in range(200):
    try:
        word1 = new_story[i]
        word2 = new_story[i+1]
        key_word = word1 + ' ' + word2
        word3 = word_dict[key_word][int(random.random() * len(word_dict[key_word]))]
        new_story.append(word3)
    except (KeyError, IndexError):
        get_seed()
        i = i + 2

print " ".join(new_story)

