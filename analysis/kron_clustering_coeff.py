import collections
import operator
import math
from nltk.corpus import brown
import networkx as nx
import matplotlib.pyplot as plt
from scipy.stats import ks_2samp
import numpy as np
import snap

#look, mommy, I did actual work
words = brown.words()
net = snap.LoadEdgeList(snap.PUNGraph, "truncated_graph.txt", 0, 1, "\t")

DegToCCfV = snap.TFltPrV()
Cf = snap.GetClustCf(net, DegToCCfV, -1)
pairs = []
for pair in DegToCCfV:
    pairs.append((pair.GetVal1(), pair.GetVal2()))
degs = map(operator.itemgetter(0), pairs)
coeffs = map(operator.itemgetter(1), pairs)

plt.loglog(degs, coeffs, 'b-')
plt.title("Clustering Coefficients on Kronecker Simulation of Brown Corpus")
plt.xlabel("Degree")
plt.ylabel("Coefficient")
plt.savefig("kron_clustering_coeff")
