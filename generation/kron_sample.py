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
from word_lib import plot_box_counts

if __name__ == "__main__":
    dim = 6 ** 7
    gen_text = "../brown_6_generated.txt"
    labels = "../6_labels.txt"
    xs = sci_sp.dok_matrix((dim, dim))
    with open(gen_text, "r") as gengraph_file:
        for line in gengraph_file.readlines():
            tup = tuple(line.split())
            xs[int(tup[0]), int(tup[1])] = 1
    print "generated graph read"
    if len(sys.argv) == 2 and sys.argv[1] == "nolabel":
        sparse_graph(xs)
    else:
        label_dict = read_labels(labels)
        labelled_xs = apply_labels(xs, label_dict)
        print "labelled xs created"
        sparse_graph(xs)
