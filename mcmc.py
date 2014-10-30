"""
Metropolis-Hastings for MCMC
"""
import numpy as np
import numpy.random as npr
import matplotlib.pyplot as plt
import operator
import random

def lnprob(x, graph, theta):
    """
    This is amenable to a trick: only compute twice in each case...
    """
    return -0.5 * np.sum(x ** 2)

def swap_nodes(ls_sigma, j, k):
    ls_sigma[k], ls_sigma[j] = ls_sigma[j], ls_sigma[k]
    return tuple(ls_sigma)

if __name__ == "__main__":
    N = 10
    sigma = tuple(range(N))
    prev_sigma = tuple(range(N))
    for i in xrange(10000)
        j = random.randint(0, N-1)
        k = random.randint(0, N-1)
        sigma = swap_nodes(list(sigma), j, k)
        u = random.random()
        if u > (lnprob(sigma, graph, theta) / lnprob(prev_sigma, graph, theta)):
            sigma = prev_sigma
    return sigma
