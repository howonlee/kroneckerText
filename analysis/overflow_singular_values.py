import collections
import math
from nltk.corpus import brown
import networkx as nx
import matplotlib.pyplot as plt
from scipy.stats import ks_2samp
import numpy as np
import numpy.linalg as npl

with open("stack_overflow2.txt", "r") as stack_corpus:
    net = nx.read_edgelist(stack_corpus)
    adj = nx.to_numpy_matrix(net)
    U, S, V = npl.svd(adj)
    eigs = S ** 2 / np.cumsum(S)[-1]
    eigs = eigs[eigs>0.0005]

    plt.loglog(eigs, 'b-')
    plt.xlabel("rank")
    plt.ylabel("singular value")
    plt.title("Singular Values from Stack Overflow Graph")
    plt.savefig("overflow_singval_loglog")
