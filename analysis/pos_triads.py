import collections
import operator
import math
from nltk.corpus import brown
import networkx as nx
import matplotlib.pyplot as plt
from scipy.stats import ks_2samp
import numpy as np
import snap

net = snap.LoadEdgeList(snap.PUNGraph, "proj/gen_pos_graph.txt", 0, 1, "\t")
TriadCntV = snap.TIntPrV()
Cf = snap.GetTriadParticip(net, TriadCntV)
pairs = []
for pair in TriadCntV:
    pairs.append((pair.GetVal1(), pair.GetVal2()))
tris = map(operator.itemgetter(0), pairs)
nodes = map(operator.itemgetter(1), pairs)

plt.loglog(tris, nodes, 'b-')
plt.title("Triangle Participation on POS Graph")
plt.xlabel("Participation")
plt.ylabel("Count")
plt.savefig("pos_triads")
