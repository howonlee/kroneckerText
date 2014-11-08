import cPickle
import word_lib
from nltk.corpus import brown

if __name__ == "__main__":
    brown_words = brown.words()[:40000]
    print len(brown_words), " words"
    bigrams = get_bigrams(brown_words)
    word_dict = word_mapping(brown_words, shuffle=False)
    mat = bigram_to_mat(bigrams, word_dict)
    print sample_from_mat(mat, 0)
