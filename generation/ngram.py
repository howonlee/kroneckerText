import cPickle
import word_lib
from nltk.corpus import brown

if __name__ == "__main__":
    brown_words = brown.words()
    print len(brown_words), " words"
    bigrams = word_lib.get_bigrams(brown_words)
    print len(set(bigrams)), " bigrams"
    #word_dict = word_lib.word_mapping(brown_words)
    #state_dict = {v:k for k, v in word_dict.iteritems()}
    #mat = word_lib.bigram_to_mat(bigrams, word_dict)
    #mat = mat.tocsr()
    #print " ".join(map(lambda x: state_dict[x], word_lib.sample_from_mat(mat, 0, num_words=2000)))
