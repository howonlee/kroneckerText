import numpy as np
import numpy.random as npr
import scipy.sparse as sci_sp
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import networkx as nx
from nltk.corpus import brown
import collections
import random

def word_mapping(words, shuffle=True):
    word_dict = {}
    curr_count = 0
    if shuffle:
        for word in words:
            if word in word_dict:
                pass #do nothing
            else:
                word_dict[word] = -1
                curr_count += 1
        #shuffle the range, we should have no -1's afterwards
        word_range = range(curr_count)
        random.shuffle(word_range)
        for key in word_dict:
            word_dict[key] = word_range.pop()
    else:
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

def get_indiv_box_count(i, j, box_size, mat):
    #this is embarrasingly parallel
    for k in xrange(0, box_size):
        for l in xrange(0, box_size):
            if mat.has_key((i + k, j + l)):
                return 1
    return 0

def get_box_count(box_size, mat):
    count = 0
    for i in xrange(0, mat.shape[0], box_size):
        for j in xrange(0, mat.shape[0], box_size):
            count += get_indiv_box_count(i, j, box_size, mat)
    return count

if __name__ == "__main__":
    brown_words = brown.words()[:4000]
    print len(brown_words)
    bigrams = get_bigrams(brown_words)
    word_dict = word_mapping(brown_words, shuffle=False)
    mat = bigram_to_mat(bigrams, word_dict)
    box_sizes = list(reversed(range(1, 500)))
    box_counts = []
    for box_size in box_sizes:
        print "getting box size ", box_size
        box_counts.append(get_box_count(box_size, mat))
    print len(box_sizes), len(box_counts)
    plt.title("box size vs. box counts, on the bigram model construed as a network")
    plt.xlabel("box size")
    plt.ylabel("box count")
    plt.loglog(box_sizes, box_counts)
    plt.show()
    """
    plt.spy(mat, markersize=0.1)
    plt.show()
    """
