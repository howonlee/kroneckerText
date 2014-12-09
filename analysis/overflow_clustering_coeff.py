import collections
import operator
import math
import matplotlib.pyplot as plt
import numpy as np
import snap

net = snap.LoadEdgeList(snap.PUNGraph, "stack_overflow.txt", 0, 1, "\t")
print net.GetNodes()
DegToCCfV = snap.TFltPrV()
Cf = snap.GetClustCf(net, DegToCCfV, -1)
pairs = []
for pair in DegToCCfV:
    pairs.append((pair.GetVal1(), pair.GetVal2()))
degs = map(operator.itemgetter(0), pairs)
print pairs
coeffs = map(operator.itemgetter(1), pairs)

plt.loglog(degs, coeffs, 'b-')
plt.title("Clustering Coefficients on Stack Overflow Network")
plt.xlabel("Degree")
plt.ylabel("Coefficient")
plt.savefig("overflow_clustering_coeff")
