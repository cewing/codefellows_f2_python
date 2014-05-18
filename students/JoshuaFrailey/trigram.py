import codecs
import random


def _build_trigram(words):
    u"""Return a dictionary of trigrams from the input text"""
    trigram = {}
    for i in range(len(words)-2):
        key = u"{} {}".format(words[i], words[i+1])
        trigram.setdefault(key, []).append(words[i+2])
    return trigram


def _file_to_list(filename):
    u"""Return list of each word in a file."""
    f = codecs.open(filename)
    lines = f.readlines()
    return u" ".join(lines).split()


def _build_story(trigram, seed=None):
    u"""Write a story from the given trigram and seed phrase; print to file."""
    if not seed:
        seed = random.choice(trigram.keys())
    f = codecs.open("tirgram.txt", "w")
    f.write(seed)
    while seed in trigram:
        next_word = random.choice(trigram[seed])
        f.write(u" {} ".format(next_word))
        new_seed = seed.split()[1:]
        new_seed.append(next_word)
        seed = u" ".join(new_seed)
    f.close()

if __name__ == "__main__":
    words = _file_to_list("sherlock_small.txt")
    trigram = _build_trigram(words)
    _build_story(trigram)