import collections
import math
from nltk.corpus import brown
import networkx as nx
import matplotlib.pyplot as plt
from scipy.stats import ks_2samp
import numpy as np

num_nodes = []
num_edges = []
i = 0;
net = nx.DiGraph()
for words in (brown.words()[x-1000:x] for x in xrange(1001, 100000, 1000)):
    i += 1
    net.add_nodes_from(words)
    for word, prevword in zip(words, words[1:]):
        net.add_edge(word, prevword)
    num_nodes.append(nx.number_of_nodes(net))
    num_edges.append(nx.number_of_edges(net))
    if i % 10 == 0:
        print "i: ", i

ks_comparison = []
for x in num_nodes:
    ks_comparison.append(x ** 1.14) #gotten by hand interpolation
plt.xlabel("number of nodes")
plt.ylabel("number of edges")
plt.plot(num_nodes, num_edges)
plt.plot(num_nodes, ks_comparison)
plt.savefig("densification_plot")

