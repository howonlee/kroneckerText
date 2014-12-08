import collections
import operator
import math
import cPickle
from nltk.corpus import brown
import networkx as nx
import matplotlib.pyplot as plt
from scipy.stats import ks_2samp
import numpy as np

net = nx.DiGraph()
tags = map(operator.itemgetter(1), brown.tagged_words())
tags_dict = {}
curr_idx = 0
for tag in tags:
    if tag not in tags_dict:
        tags_dict[tag] = curr_idx
        curr_idx += 1
net.add_nodes_from(tags_dict.values())
#for word, prevword in zip(tags, tags[1:]):
#    net.add_edge(tags_dict[word], tags_dict[prevword])
#nx.write_edgelist(net, "brown_pos_graph.txt", data=False)
with open("pos_dict.pickle", "wb") as pickle_file:
    cPickle.dump(tags_dict, pickle_file)
