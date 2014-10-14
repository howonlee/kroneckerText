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

from kronecker import generate, stochastic_kronecker

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

if __name__ == "__main__":
    dim = 256 #power of 2
    k_probs = np.array([0.4504, 0.2511, 0.2279, 0.0706])
    xs = np.zeros((dim, dim))
    xs = generate(xs, dim, 2000, k_probs)
    xs = stochastic_kronecker(xs, dim)
    D = nx.DiGraph(xs)
    D = get_brown_freqs(D)
    print " ".join(sample_from_graph(D))
    print "====================="
    print "====================="
