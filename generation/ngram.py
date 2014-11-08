import cPickle
import word_lib
from nltk.corpus import brown

if __name__ == "__main__":
    brown_words = brown.words()[:40000]
    print len(brown_words), " words"
    bigrams = word_lib.get_bigrams(brown_words)
    word_dict = word_lib.word_mapping(brown_words, shuffle=False)
    mat = word_lib.bigram_to_mat(bigrams, word_dict)
    mat = mat.tocsr()
    print word_lib.sample_from_mat(mat, 0)
