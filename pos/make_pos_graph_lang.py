import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

if __name__ == "__main__":
    net = nx.read_edgelist("../gen_pos_graph.txt")
    adj = nx.to_numpy_matrix(net)
    #make the labels
