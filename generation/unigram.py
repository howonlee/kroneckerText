from __future__ import print_function
from nltk.corpus import brown
import random

if __name__ == "__main__":
    words = brown.words()
    for x in xrange(10000):
        print(random.choice(words) + " ", end="")
