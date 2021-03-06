import collections
import math
from nltk.corpus import brown
import networkx as nx
import matplotlib.pyplot as plt
from scipy.stats import ks_2samp
import numpy as np
import numpy.linalg as npl

with open("miller_corpus.txt", "r") as miller_corpus:
    net = nx.DiGraph()
    words = miller_corpus.read().split()[:10000]
    net.add_nodes_from(words)
    for word, prevword in zip(words, words[1:]):
        net.add_edge(word, prevword)
    adj = nx.to_numpy_matrix(net)
    plt.matshow(adj)
    plt.title("Singular Values from Miller Corpus Graph")
    plt.savefig("miller_adj_mat")
