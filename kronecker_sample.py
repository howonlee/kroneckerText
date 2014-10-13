import snap
import numpy as np
import numpy.random as npr
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import networkx as nx
from nltk.corpus import brown
import collections
from operator import itemgetter
from random import choice

def get_brown_freqs(net):
    counts = collections.Counter(brown.words())
    freq_counts = counts.most_common()
    for i, node in enumerate(sorted(net.degree_iter(), key=itemgetter(1), reverse=True)):
        node_id, _ = node
        net.node[node_id]["word"] = freq_counts[i][0]
    return net

def sample_from_graph(net):
    words = []
    curr_node = choice(net.nodes())
    for i in xrange(400):
        words.append(net.node[curr_node]["word"])
        neighs = net.neighbors(curr_node)
        if neighs:
            curr_node = choice(neighs)
        else:
            curr_node = choice(net.nodes())
    return words


def generate(arr, dim, num_points, probs):
    for i in xrange(num_points):
        curr_dim = dim
        curr_view = arr.view()
        while curr_dim > 1:
            half_dim = curr_dim // 2
            curr_draw = npr.choice(4, p=probs)
            if curr_draw == 0:
                curr_view = curr_view[:half_dim, :half_dim]
            if curr_draw == 1:
                curr_view = curr_view[half_dim:, :half_dim]
            if curr_draw == 2:
                curr_view = curr_view[:half_dim, half_dim:]
            if curr_draw == 3:
                curr_view = curr_view[half_dim:, half_dim:]
            curr_dim = half_dim
            if curr_dim == 1:
                curr_view[0,0] = 1
    return arr

if __name__ == "__main__":
    dim = 512 #power of 2
    #for i in list(np.arange(0,0.5,0.1)):
    k_probs = np.array([0.25, 0.25, 0.25, 0.25])
    xs = np.zeros((dim, dim))
    xs = generate(xs, dim, 10000, k_probs)
    D = nx.DiGraph(xs)
    D = get_brown_freqs(D)
    print " ".join(sample_from_graph(D))
    print "====================="
    print "====================="
