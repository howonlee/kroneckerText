import cPickle
from lib_kron import *
import word_lib
import sys
from nltk.corpus import brown

if __name__ == "__main__":
    dim = 2**16
    gen_text = "../brown_2_generated.txt"
    labels = "../2_labels.txt"
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
    labelled_xs = apply_labels(xs, label_dict)
    labelled_xs = labelled_xs[:51156,:51156]
    labelled_xs = labelled_xs.tocsr()
    print "labelled xs created"
    sample = word_lib.sample_from_mat(labelled_xs, 1)
    print " ".join([state_dict[x] for x in sample])
