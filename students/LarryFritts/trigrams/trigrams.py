"""Trigrams Assignment"""

import codecs
import random
import string


def get_seed(seed_words):
    """Provides a key value to start a new story or recover from dead-end"""
    seed_phrase = random.choice(seed_words).split()
    word0 = seed_phrase[0]
    word1 = seed_phrase[1]
    new_story.append(word0)
    new_story.append(word1)

if __name__ == "__main__":
    word_dict = {}
    new_story = []

    """Open text file, strip punc, make it a list"""
    f = codecs.open("sherlock.txt", 'r')
    story_w_punc = f.read()
    story = ""
    for ch in story_w_punc:
        if ch not in string.punctuation:
            story = story + ch
    f.close()
    story = story.lower().split()

    """Create the trigram dictionary"""
    for i in range(len(story)-3):
        word1 = story[i]
        word2 = story[i+1]
        word3 = story[i+2]
        word_dict.setdefault(word1 + ' ' + word2, []).append(word3)
    seed_words = word_dict.keys()

    """Build a story using the trigrams"""
    for i in range(len(story)):
        try:
            word1 = new_story[i]
            word2 = new_story[i+1]
            key_word = word1 + ' ' + word2
            word3 = random.choice(word_dict[key_word])
            new_story.append(word3)
        except (KeyError, IndexError):
            get_seed(seed_words)
            i = i + 2

    print " ".join(new_story)

