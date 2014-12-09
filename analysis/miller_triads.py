import collections
import operator
import math
from nltk.corpus import brown
import networkx as nx
import matplotlib.pyplot as plt
from scipy.stats import ks_2samp
import numpy as np
import snap

with open("miller_corpus.txt", "r") as miller_file:
    words = miller_file.read().split()
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

    TriadCntV = snap.TIntPrV()
    Cf = snap.GetTriadParticip(net, TriadCntV)
    pairs = []
    for pair in TriadCntV:
        pairs.append((pair.GetVal1(), pair.GetVal2()))
    tris = map(operator.itemgetter(0), pairs)
    nodes = map(operator.itemgetter(1), pairs)

    plt.loglog(tris, nodes, 'b-')
    plt.title("Triangle Participation Ratios on Miller Graph")
    plt.xlabel("Participation")
    plt.ylabel("Count")
    plt.savefig("miller_triads")
