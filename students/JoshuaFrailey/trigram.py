import codecs
import random
import string


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


def _collect_stats(words):
    stats = {}
    punctuation_dict = {punc: 0 for punc in string.punctuation}
    punctuation_dict[u"Capital"] = 0
    punctuation_dict[u"None"] = 0
    punctuation_dict[u"Count"] = 0
    for word in words:
        if word[0].isupper():
            try:
                stats[word.lower()][u"Capital"] += 1
                stats[word.lower()][u"Count"] += 1
            except KeyError:
                stats.setdefault(word.lower(), punctuation_dict.copy())[u"Capital"] += 1
                stats[word.lower()][u"Count"] += 1
        word = word.lower()
        if word[-1] in string.punctuation:
            try:
                stats[word[:-1]][word[-1]] += 1
                stats[word[:-1]][u"Count"] += 1
            except KeyError:
                stats.setdefault(word[:-1], punctuation_dict.copy())[word[-1]] += 1
                stats[word[:-1]][u"Count"] += 1
        else:
            try:
                stats[word][u"None"] += 1
                stats[word][u"Count"] += 1
            except KeyError:
                stats.setdefault(word, punctuation_dict.copy())[u"None"] += 1
                stats[word][u"Count"] += 1
    return stats


if __name__ == "__main__":
    words = _file_to_list("sherlock_small.txt")
    trigram = _build_trigram(words)
    _build_story(trigram)