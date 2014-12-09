import collections
import math
from nltk.corpus import brown
import networkx as nx
import matplotlib.pyplot as plt
from scipy.stats import ks_2samp
import numpy as np

with open("miller_corpus.txt", "r") as miller_corpus:
    net = nx.DiGraph()
    words = miller_corpus.read().split()
    net.add_nodes_from(words)
    for word, prevword in zip(words, words[1:]):
        net.add_edge(word, prevword)
    degree_sequence=sorted(nx.degree(net).values(),reverse=True)
    plt.loglog(degree_sequence, 'b-')
    plt.title("Degree Counts on Miller-Generated Words")
    plt.xlabel("Degree")
    plt.ylabel("Count")
    plt.savefig("miller_degree_plot")

