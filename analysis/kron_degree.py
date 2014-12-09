import collections
import operator
import math
from nltk.corpus import brown
import networkx as nx
import matplotlib.pyplot as plt
from scipy.stats import ks_2samp
import numpy as np

net = nx.read_edgelist("../truncated_graph.txt")
degree_sequence=sorted(nx.degree(net).values(),reverse=True)
plt.loglog(degree_sequence, 'b-')
plt.title("Degree Counts on Stochastic Kronecker Graph")
plt.xlabel("Degree")
plt.ylabel("Count")
plt.savefig("kron_degree_plot")
