import nltk
import perceptron

#inspired by M honnibal's implementation, honnibal.wordpress.com/2013/09/11/

class PerceptronTagger(object):
    def __init__(self):
        self.model = AveragedPerceptron()
        self.tagdict = {}
        self.classes = set()

    def tag(self, corpus, tokenize=True):
        s_split = split the corpus into sentences
        w_split = split the corpus into word tokens
        def sentence_generator(corpus):
            for s in s_split(corpus):
                yield w_split(s)
        prev, prev2 = self.START
        tokens = []
        for words in sentence_generator(corpus):
            pass #################

    def train(self, sentences, nr_iter=5):
        pass

    def _normalize(self, word):
        pass

    def _get_features(self, i, word, context, prev, prev2):
        pass

    def _make_tagdict(self, sentences):
        pass

if __name__ == "__main__":
    pass
