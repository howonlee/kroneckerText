import collections
import operator
import math
from nltk.corpus import brown
import networkx as nx
import matplotlib.pyplot as plt
from scipy.stats import ks_2samp
import numpy as np

net = nx.DiGraph()
tags = map(operator.itemgetter(1), brown.tagged_words())
net.add_nodes_from(tags)
for word, prevword in zip(tags, tags[1:]):
    net.add_edge(word, prevword)
degree_sequence=sorted(nx.degree(net).values(),reverse=True)
plt.loglog(degree_sequence, 'b-')
plt.title("Degree Counts on Brown POS Tags")
plt.xlabel("Degree")
plt.ylabel("Count")
plt.savefig("pos_degree_plot")
