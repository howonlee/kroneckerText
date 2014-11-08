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
