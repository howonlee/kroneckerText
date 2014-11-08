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
from itertools import izip

def sort_coo(m):
    tuples = izip(m.row, m.col, m.data)
    return sorted(tuples, key=lambda x: (x[0], x[2]))

def get_brown_freqs(net):
    counts = collections.Counter(brown.words())
    freq_counts = counts.most_common()
    for i, node in enumerate(sorted(net.degree_iter(), key=itemgetter(1), reverse=True)):
        node_id, _ = node
        net.node[node_id]["word"] = freq_counts[i][0]
    return net

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

def sample_from_graph(net):
    """
    Not really optimal
    """
    words = []
    curr_node = choice(net.nodes())
    for i in xrange(400):
        words.append(net.node[curr_node]["word"])
        neighs = net.neighbors(curr_node)
        #choose these weighted on the neighbors' indegree, instead of randomly
        if neighs:
            curr_node = choice(neighs)
        else:
            curr_node = choice(net.nodes())
    return words

def sparse_graph(mat):
    plt.spy(mat, markersize=0.2)
    plt.show()

def apply_labels(old_xs, label_dict):
    labelled_xs = sci_sp.dok_matrix(old_xs.shape)
    for key in old_xs.iterkeys():
        curr_first = key[0]
        if key[0] in label_dict:
            curr_first = label_dict[key[0]]
        curr_second = key[1]
        if key[1] in label_dict:
            curr_second = label_dict[key[1]]
        labelled_xs[curr_first, curr_second] = 1
    return labelled_xs

def read_labels(filename="2_labels.txt"):
    labels = []
    label_dict = {}
    with open(filename, "r") as labels_file:
        labels = map(int, labels_file.read().split())
    print "labels read: file: ", filename
    for idx, label in enumerate(labels):
        label_dict[idx] = label
    return label_dict
