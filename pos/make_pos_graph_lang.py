import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

if __name__ == "__main__":
    net = nx.read_edgelist("../gen_pos_graph.txt")
    adj = nx.to_numpy_matrix(net)
    #assign the labels... there's some previous code for this
    #then, take it as a Markov chain. How?
    #how would the Markov chain be turned into a matrix again?

