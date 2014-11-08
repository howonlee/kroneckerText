import collections
import itertools
import random
import matplotlib.pyplot as plt
import cPickle

def get_ngram(corpus, n):
    return itertools.izip(*[corpus[i:] for i in xrange(n)])

if __name__ == "__main__":
    brown_words = []
    with open("brown.txt", "r") as brown_file:
        brown_words = cPickle.load(brown_file)
    num_n = range(1,10)
    ngram_counters = {x, collection.Counter() for x in xrange(1,10)}
    for i in num_n:
        for ngram in get_ngram(brown_words, i):
            ngram_counters[i][ngram] += 1
    for i in num_n:
        plt.plot(something)
    plt.show()
