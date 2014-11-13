import collections
import math
from nltk.corpus import brown
import networkx as nx
import matplotlib.pyplot as plt
from scipy.stats import ks_2samp
import numpy as np

net = nx.DiGraph()
words = brown.words()[:500000]
net.add_nodes_from(words)
for word, prevword in zip(words, words[1:]):
    net.add_edge(word, prevword)
degree_sequence=sorted(nx.degree(net).values(),reverse=True)
plt.loglog(degree_sequence, 'b-')
plt.title("degree loglog histogram")
plt.show()

