import cPickle

if __name__ == "__main__":
    nodeperm_dict = {}
    with open("gen_pos_graph_nodeperm", "r") as nodeperm_file:
        perms = map(int, nodeperm_file.read().split())
        for idx, perm in enumerate(perms):
            nodeperm_dict[idx] = perm
    with open("pos_nodeperm_dict.pickl", "wb") as pickle_file:
        cPickle.dump(nodeperm_dict, pickle_file)
