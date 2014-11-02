import numpy as np
import numpy.random as npr
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import networkx as nx
from nltk.corpus import brown
import collections
from operator import itemgetter
from random import choice
import random
import sys

from lib_kron import *
from fractal_dimension import plot_box_counts

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
        #choose these weighted on the neighbors' indegree, instead of randomly
        if neighs:
            curr_node = choice(neighs)
        else:
            curr_node = choice(net.nodes())
    return words

def sparse_graph(mat):
    plt.spy(mat, markersize=0.2)
    plt.show()

if __name__ == "__main__":
    k_probs = np.array([[0.06497, 0.4972, 0.03143, 0.1481], [0.5009, 0.9999, 0.3081, 0.7603], [0.03298, 0.3063, 0.02129, 0.07878], [0.154, 0.7644, 0.08075, 0.3984]])
    xs = create_generator(k_probs, 4)
    xs = generate_weighted(xs)
    if len(sys.argv) == 2 and sys.argv[1] == "graph":
        sparse_graph(xs)
    else:
        D = nx.DiGraph(xs)
        D = get_brown_freqs(D)
        print " ".join(sample_from_graph(D))
        print "====================="
        print "====================="
