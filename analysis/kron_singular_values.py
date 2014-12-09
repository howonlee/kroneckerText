import collections
import operator
import math
from nltk.corpus import brown
import networkx as nx
import matplotlib.pyplot as plt
from scipy.stats import ks_2samp
import numpy as np
import numpy.linalg as npl

net = nx.read_edgelist("truncated_2_graph.txt")
adj = nx.to_numpy_matrix(net)
U, S, V = npl.svd(adj)
eigs = S ** 2 / np.cumsum(S)[-1]
eigs = eigs[eigs>0.0005]

plt.loglog(eigs, 'b-')
plt.xlabel("rank")
plt.ylabel("singular value")
plt.title("Singular Values of Stochastic Kronecker Graph")
plt.savefig("kron_singval_loglog")
