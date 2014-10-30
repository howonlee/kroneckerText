import cPickle
import scipy.sparse as sci_sp
import numpy as np
import itertools
import random
import math
import collections
import matplotlib.pyplot as plt

def plot_sparse(mat):
    plt.spy(mat, markersize=0.1)
    plt.show()

def plot_lognormal(mat):
    degrees = mat.sum(axis=1)
    degrees = list(np.sort(np.ravel(degrees)))
    degrees.reverse()
    degrees = map(lambda x: math.log(x), degrees)
    plt.plot(range(len(degrees)),degrees)
    plt.show()

def plot_powerlaw(mat):
    degrees = mat.sum(axis=0)
    degrees = list(np.sort(np.ravel(degrees)))
    degrees.reverse()
    plt.loglog(range(len(degrees)),degrees)
    plt.show()

def plot_degrees_powerlaw(degrees):
    degrees = sorted(degrees)
    degrees.reverse()
    plt.loglog(range(len(degrees)),degrees)
    plt.show()

def thresh_mat(mat):
    return mat.multiply(mat>3)

if __name__ == "__main__":
    gutenberg_states = []
    with open("brown_states.txt", "r") as states_file:
        gutenberg_states = cPickle.load(states_file)
    gutenberg_states = gutenberg_states[:10000]
    len_gut = len(gutenberg_states)
    sp_statemat = sci_sp.dok_matrix((len_gut, len_gut))
    state = 0
    word_dict = collections.Counter()
    #we can have the powerlaw...
    for idx, word in enumerate(gutenberg_states):
        word_dict[word] += 1
