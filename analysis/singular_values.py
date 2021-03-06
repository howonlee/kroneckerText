import collections
import math
from nltk.corpus import brown
import networkx as nx
import matplotlib.pyplot as plt
from scipy.stats import ks_2samp
import numpy as np
import numpy.linalg as npl

net = nx.DiGraph()
words = brown.words()[:5000]
net.add_nodes_from(words)
for word, prevword in zip(words, words[1:]):
    net.add_edge(word, prevword)
adj = nx.to_numpy_matrix(net)
U, S, V = npl.svd(adj)
eigs = S ** 2 / np.cumsum(S)[-1]
eigs = eigs[eigs>0.0005]

plt.loglog(eigs, 'b-')
plt.xlabel("rank")
plt.ylabel("singular value")
plt.title("Singular Values of Brown Corpus Graph")
plt.savefig("singval_loglog")
