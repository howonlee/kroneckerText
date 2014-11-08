import cPickle
import lib_kron
from nltk.corpus import brown

if __name__ == "__main__":
    xs = sci_sp.dok_matrix((6**7, 6**7))
    with open("brown_6_generated.txt", "r") as gengraph_file:
        for line in gengraph_file.readlines():
            tup = tuple(line.split())
            xs[int(tup[0]), int(tup[1])] = 1
    print "generated graph read"
    if len(sys.argv) == 2 and sys.argv[1] == "graph":
        sparse_graph(xs)
    else:
        label_dict = read_labels("6_labels.txt")
        labelled_xs = apply_labels(xs, label_dict)
        print "labelled xs created"


    brown_words = brown.words()[:40000]
    print len(brown_words), " words"
    bigrams = word_lib.get_bigrams(brown_words)
    word_dict = word_lib.word_mapping(brown_words, shuffle=False)
    state_dict = {v:k for k, v in word_dict.iteritems()}
    mat = word_lib.bigram_to_mat(bigrams, word_dict)
    mat = mat.tocsr()
    print " ".join(map(lambda x: state_dict[x], word_lib.sample_from_mat(mat, 0)))
