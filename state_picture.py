import cPickle
import scipy.sparse as sci_sp
import numpy as np
import itertools
import random
import matplotlib.pyplot as plt

def plot_sparse(mat):
    plt.spy(mat, markersize=0.1)
    plt.show()

def plot_powerlaw(mat):
    degrees = mat.sum(axis=1)
    degrees = list(np.sort(np.ravel(degrees)))
    degrees.reverse()
    plt.loglog(range(len(degrees)),degrees)
    plt.show()

if __name__ == "__main__":
    gutenberg_states = []
    with open("brown_states.txt", "r") as states_file:
        gutenberg_states = cPickle.load(states_file)
    gutenberg_states = gutenberg_states[:400000]
    max_gut_state = max(gutenberg_states)
    print max_gut_state
    sp_statemat = sci_sp.dok_matrix((max_gut_state+1, max_gut_state+1))
    uni, bi = itertools.tee(gutenberg_states)
    bi.next()
    state = 0
    for x, y in itertools.izip(uni, bi):
        state += 1
        sp_statemat[x,y] += 1
        if state % 10000 == 0:
            print "state: ", state
    #threshholding
    sp_statemat = sp_statemat.multiply(sp_statemat>3)
    #plot_sparse(sp_statemat)
    plot_powerlaw(sp_statemat)
