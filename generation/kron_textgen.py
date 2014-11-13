import cPickle
from lib_kron import *
import word_lib
import matplotlib.pyplot as plt
import sys
from nltk.corpus import brown

def process_xs(xs, len_labeldict=51156):
    labelled_xs = apply_labels(xs, label_dict)
    labelled_xs = labelled_xs[:len_labeldict,:len_labeldict]
    labelled_xs = labelled_xs.tocsr()
    return labelled_xs

if __name__ == "__main__":
    """
    Remember the indexing of the labels and how that works: how does that work, anyways?
    """
    dim = 6**7
    gen_text = "../brown_6_generated.txt"
    labels = "../6_labels.txt"
    with open("../brown.txt") as brown_file:
        brown_words = cPickle.load(brown_file)
    print len(brown_words), " words"
    word_dict = word_lib.word_mapping(brown_words)
    state_dict = {v:k for k, v in word_dict.iteritems()}
    print len(state_dict)
    xs = sci_sp.dok_matrix((dim, dim))
    with open(gen_text, "r") as gengraph_file:
        for line in gengraph_file.readlines():
            tup = tuple(line.split())
            xs[int(tup[0]), int(tup[1])] = 1
    print "generated graph read"
    label_dict = read_labels(labels)
    labelled_xs = process_xs(xs)
    print "labelled xs created"
    sample = word_lib.sample_from_mat(labelled_xs, 1, num_words=10000)
    print " ".join([state_dict[x] for x in sample])
