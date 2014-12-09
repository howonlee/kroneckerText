import collections
import math
from nltk.corpus import brown
import networkx as nx
import matplotlib.pyplot as plt
from scipy.stats import ks_2samp
import numpy as np

with open("stack_overflow.txt", "r") as stack_corpus:
    net = nx.read_edgelist(stack_corpus)
    degree_sequence=sorted(nx.degree(net).values(),reverse=True)
    plt.loglog(degree_sequence, 'b-')
    plt.title("Degree Counts on Stack Overflow Users")
    plt.xlabel("Degree")
    plt.ylabel("Count")
    plt.savefig("overflow_degree_plot")

