import collections
import math
from nltk.corpus import brown
import networkx as nx
import matplotlib.pyplot as plt
from scipy.stats import ks_2samp
import numpy as np

diams = []
for words in (brown.words()[:x] for x in xrange(501, 15000, 500)):
    net = nx.DiGraph()
    net.add_nodes_from(words)
    for word, prevword in zip(words, words[1:]):
        net.add_edge(word, prevword)
    try:
        diams.append(nx.diameter(net))
    except nx.NetworkXError:
        diams.append(-1)
    del net
    print "i done"
diams = filter(lambda x: x != -1, diams)
plt.title("diameter progression with respect to number of words in graph")
plt.plot(diams, 'b-')
plt.show()

