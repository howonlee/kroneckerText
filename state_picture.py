import cPickle
import scipy.sparse as sci_sp
import numpy as np
import itertools
import random
import collections
import math
import matplotlib.pyplot as plt

def plot_sparse(mat):
    plt.spy(mat, markersize=0.1)
    plt.show()

def plot_lognormal(mat):
    degrees = mat.sum(axis=1)
    degrees = list(np.sort(np.ravel(degrees)))
    degrees.reverse()
    degrees = map(lambda x: math.exp(x), degrees)
    plt.plot(range(len(degrees)),degrees)
    plt.show()

def plot_powerlaw(mat):
    degrees = mat.sum(axis=1)
    degrees = degrees.sum(axis=1)
    degrees = list(np.sort(np.ravel(degrees)))
    degrees.reverse()
    plt.loglog(range(len(degrees)),degrees)
    plt.show()

def thresh_mat(mat):
    return mat.multiply(mat>3)

def plot_degrees_powerlaw(degrees):
    degrees = sorted(degrees)
    degrees.reverse()
    plt.loglog(range(len(degrees)),degrees)
    plt.show()

if __name__ == "__main__":
    gutenberg_states = []
    with open("brown_states.txt", "r") as states_file:
        gutenberg_states = cPickle.load(states_file)
    #gutenberg_states = gutenberg_states[:7000]
    max_gut_state = max(gutenberg_states)
    print max_gut_state
    sp_statemat = collections.Counter()
    uni, bi, tri, quad= itertools.tee(gutenberg_states, 4)
    bi.next()
    tri.next(); tri.next()
    quad.next(); quad.next(); quad.next()
    state = 0
    for x, y, z, xx in itertools.izip(uni, bi, tri, quad):
        state += 1
        sp_statemat[(x,y,z,xx)] += 1
        if state % 10000 == 0:
            print "state: ", state
    #plot_sparse(sp_statemat)
    #plot_powerlaw(sp_statemat)
    #plot_lognormal(sp_statemat)
    plot_degrees_powerlaw([y for x,y in sp_statemat.most_common()])
