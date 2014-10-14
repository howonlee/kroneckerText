import numpy as np
import numpy.random as npr
import scipy.sparse as sci_sp
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import random

from lib_kron import generate, stochastic_kronecker

if __name__ == "__main__":
    k1_probs = np.array([0.25, 0.25, 0.25, 0.25]) #unrolled
    dim = 2048 #power of 2
    xs = sci_sp.dok_matrix((dim,dim))
    xs = generate(xs, dim, 1000, k1_probs)
    kron_mat = stochastic_kronecker(xs, dim) #still in dok
