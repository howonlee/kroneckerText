"""
Kronecker graph generation lib
"""
import numpy as np
import numpy.random as npr
import scipy.sparse as sci_sp
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import random

def generate(arr, dim, num_points, probs):
    """
    Try to get the arr to be sparse
    """
    for i in xrange(num_points):
        x_bounds = [0, dim]
        y_bounds = [0, dim]
        curr_dim = dim
        #unroll this shit? it's the inner loop
        while curr_dim > 1:
            half_dim = curr_dim // 2
            curr_draw = npr.choice(4, p=probs)
            if curr_draw == 0:
                x_bounds[0] += half_dim
                y_bounds[0] += half_dim
            if curr_draw == 1:
                x_bounds[0] += half_dim
                y_bounds[1] -= half_dim
            if curr_draw == 2:
                x_bounds[1] -= half_dim
                y_bounds[0] += half_dim
            if curr_draw == 3:
                x_bounds[1] -= half_dim
                y_bounds[1] -= half_dim
            curr_dim = half_dim
            if curr_dim == 1:
                arr[x_bounds[0],y_bounds[0]] = 1 #they should be the same
    return arr

def stochastic_kronecker(arr, dim, alpha=0.8, beta=0.2):
    """
    Actually draws from the stochastic kronecker distribution
    Returns a dok sparse matrix
    """
    k_mat = sci_sp.dok_matrix((arr.shape[0], arr.shape[1]))
    for i in xrange(dim):
        for j in xrange(dim):
            if arr[i,j] == 0 and random.random() < beta:
                k_mat[i,j] = 1
            if arr[i,j] == 1 and random.random() < alpha:
                k_mat[i,j] = 1
    return k_mat
