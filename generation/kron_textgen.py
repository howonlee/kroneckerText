import cPickle
from lib_kron import *
import word_lib
import sys
from nltk.corpus import brown

if __name__ == "__main__":
    with open("../brown.txt") as brown_file:
        brown_words = cPickle.load(brown_file)
    print len(brown_words), " words"
    word_dict = word_lib.word_mapping(brown_words)
    state_dict = {v:k for k, v in word_dict.iteritems()}
    print len(state_dict)
    xs = sci_sp.dok_matrix((6**7, 6**7))
    with open("../brown_6_generated.txt", "r") as gengraph_file:
        for line in gengraph_file.readlines():
            tup = tuple(line.split())
            xs[int(tup[0]), int(tup[1])] = 1
    print "generated graph read"
    label_dict = read_labels("../6_labels.txt")
    #labelled_xs = apply_labels(xs, label_dict)
    xs = xs[:51156,:51156]
    xs = xs.tocsr()
    print "labelled xs created"
    sample = word_lib.sample_from_mat(xs, 1)
    print " ".join([state_dict[x] for x in sample])
