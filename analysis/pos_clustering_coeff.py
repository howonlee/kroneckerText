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
words = map(operator.itemgetter(1), brown.tagged_words())
net = snap.TUNGraph.New()
word_dict = {}
curr_idx = 0
for word in words:
    if word not in word_dict:
        word_dict[word] = curr_idx
        net.AddNode(curr_idx)
        curr_idx += 1
for word, prevword in zip(words, words[1:]):
    net.AddEdge(word_dict[word], word_dict[prevword])

DegToCCfV = snap.TFltPrV()
Cf = snap.GetClustCf(net, DegToCCfV, -1)
pairs = []
for pair in DegToCCfV:
    pairs.append((pair.GetVal1(), pair.GetVal2()))
degs = map(operator.itemgetter(0), pairs)
coeffs = map(operator.itemgetter(1), pairs)

plt.loglog(degs, coeffs, 'b-')
plt.title("Clustering Coefficients on Brown POS Tags")
plt.xlabel("Degree")
plt.ylabel("Coefficient")
plt.savefig("pos_clustering_coeff")
