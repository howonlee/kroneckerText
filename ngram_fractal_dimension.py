import collections
import itertools
import random
import cPickle

def get_ngram(corpus, n):
    return itertools.izip(*[corpus[i:] for i in xrange(n)])

def unique(iterable):
    seen = set()
    for item in iterable:
        if item in seen:
            continue
        seen.add(item)
        yield item

if __name__ == "__main__":
    brown_words = []
    with open("brown.txt", "r") as brown_file:
        brown_words = cPickle.load(brown_file)
    num_n = range(1,5)
    num_ngrams = []
    for i in num_n:
        num_ngrams.append(sum(1 for _ in unique(get_ngram(brown_words, i))))
    for n, ngrams in zip(num_n, num_ngrams):
        print "(%d, %d)" % (n, ngrams)
