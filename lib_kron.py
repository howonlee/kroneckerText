"""
Kronecker graph generation lib
"""
import numpy as np
import numpy.random as npr
import scipy.sparse as sci_sp
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import random
import pymc

def create_generator(generator, exponent):
    """
    Create the dense kronecker distributional array
    """
    arr = generator.copy()
    for x in xrange(exponent):
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

def kron_fit():
    """
    Kronecker fit on not too big a space
    """
    pass

def kron_em():
    """
    Kronecker em
    """
    pass
