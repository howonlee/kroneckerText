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

if __name__ == "__main__":
    xs = sci_sp.dok_matrix((6**7, 6**7))
    with open("brown_6_generated.txt", "r") as gengraph_file:
        for line in gengraph_file.readlines():
            tup = tuple(line.split())
            xs[int(tup[0]), int(tup[1])] = 1
    print "generated graph read"
    if len(sys.argv) == 2 and sys.argv[1] == "graph":
        sparse_graph(xs)
    else:
        label_dict = read_labels("6_labels.txt")
        labelled_xs = apply_labels(xs, label_dict)
        print "labelled xs created"
        sparse_graph(labelled_xs)
        """
        Change this bit
        D = nx.DiGraph(xs)
        D = get_brown_freqs(D)
        print " ".join(sample_from_graph(D))
        """
