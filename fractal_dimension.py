import numpy as np
import numpy.random as npr
import scipy.sparse as sci_sp
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import networkx as nx
from nltk.corpus import brown
import collections
from operator import itemgetter
from random import choice
import random

def word_mapping(words):
    word_dict = {}
    curr_count = 0
    for word in words:
        if word in word_dict:
            pass #do nothing
        else:
            word_dict[word] = curr_count
            curr_count += 1
    return word_dict

def get_bigrams(ls):
    return zip(ls, ls[1:])

def bigram_to_mat(bigram, word_map):
    mat = sci_sp.dok_matrix((len(word_map), len(word_map)))
    for prevword, word in bigram:
        mat[word_map[prevword], word_map[word]] += 1
    return mat

if __name__ == "__main__":
    brown_words = brown.words()
    print len(brown_words)
    bigrams = get_bigrams(brown_words)
    word_dict = word_mapping(brown_words)
    mat = bigram_to_mat(bigrams, word_dict)
    plt.spy(mat, markersize=0.3)
    plt.show()

    #get the bigram matrix, create that sucker
    #normalize
    #bound it via like 0.005 or something
    #count that fractal dimension via boxes
    #probably can also count lacunarity via box counting
    #and then use it for nice things
