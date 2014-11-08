"""
Kronecker graph generation lib
"""
import numpy as np
import numpy.random as npr
import scipy.sparse as sci_sp
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import random
import emcee
import gc
from nltk.corpus import brown

def create_generator(generator, exponent):
    """
    Do the sparsification at each point?
    Calculate things out-of-memory like in the actual implementation?
    """
    arr = generator.copy()
    for x in xrange(exponent):
        print "creating generator for exponent ... ", x
        print arr.shape
        gc.collect()
        arr = np.kron(arr, generator)
    return arr

def generate(arr):
    k_mat = sci_sp.dok_matrix(arr.shape)
    for i in xrange(arr.shape[0]):
        for j in xrange(arr.shape[0]):
            rand = random.random()
            if rand < arr[i,j]:
                k_mat[i,j] = 1
    return k_mat

def generate_weighted(arr):
    k_mat = np.zeros(arr.shape)
    for i in xrange(arr.shape[0]):
        for j in xrange(arr.shape[0]):
            rand = random.random()
            if rand > arr[i,j]:
                k_mat[i,j] = 0
            else:
                k_mat[i,j] = arr[i,j]
    return k_mat
