import snap
import numpy as np
import numpy.random as npr
import scipy.sparse as sci_sp
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import networkx as nx
import random

def generate(arr, dim, num_points):
    for i in xrange(num_points):
        x_bounds = [0, dim]
        y_bounds = [0, dim]
        curr_dim = dim
        #unroll this shit? it's the inner loop
        while curr_dim > 1:
            half_dim = curr_dim // 2
            curr_draw = npr.choice(4, p=k1_probs)
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

def stochastic_kronecker(dense_mat, dim, alpha=0.8, beta=0.2):
    k_mat = np.zeros_like(dense_mat)
    for i in xrange(dim):
        for j in xrange(dim):
            if dense_mat[i,j] == 0 and random.random() < beta:
                k_mat[i,j] = 1
            if dense_mat[i,j] == 1 and random.random() < alpha:
                k_mat[i,j] = 1
    return k_mat

def plot_kronecker(dense_mat):
    plt.imshow(dense_mat)
    plt.show()

def plot_graph(dense_mat):
    net = nx.DiGraph(dense_mat)
    nx.draw(net)
    plt.show()

def plot_graph_indegrees(dense_mat):
    net = nx.DiGraph(dense_mat)
    degree_sequence=sorted(nx.degree(net).values(),reverse=True) # degree sequence
    plt.loglog(degree_sequence, 'b-')
    plt.title("degree rank plot")
    plt.ylabel("degree")
    plt.xlabel("rank")
    plt.show()

if __name__ == "__main__":
    k1_probs = np.array([0.25, 0.25, 0.25, 0.25]) #unrolled
    dim = 2048 #power of 2
    xs = sci_sp.dok_matrix(np.zeros((dim, dim)))
    xs = generate(xs, dim, 1000)
    xs_dense = xs.todense()
    k_dense = stochastic_kronecker(xs_dense, dim)
    plot_graph_indegrees(xs_dense)
