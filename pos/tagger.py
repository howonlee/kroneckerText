#Honnibal's Greedy Averaged Perceptron Tagger
from __future__ import absolute_import
import os
import random
from collections import defaultdict
import pickle
import logging
import operator
import itertools
import networkx as nx

from textblob.base import BaseTagger
from textblob.tokenizers import WordTokenizer, SentenceTokenizer
from textblob.exceptions import MissingCorpusError
from perceptron import AveragedPerceptron

PICKLE = "baseline_res"

class PerceptronTagger(BaseTagger):
    START = ['-START-', '-START2-']
    END = ['-END-', '-END2-']
    AP_MODEL_LOC = os.path.join(os.path.dirname(__file__), PICKLE)

    def __init__(self, load=True):
        self.model = AveragedPerceptron()
        self.tagdict = {}
        self.classes = set()
        self.graphdict = pickle.load(open("../pos_dict.pickle", "rb"))
        self.nodeperm = pickle.load(open("../pos_nodeperm_dict.pickle", "rb"))
        self.graph = nx.DiGraph()
        if load:
            self.load(self.AP_MODEL_LOC)
        with open("../gen_pos_graph.txt", "r") as pos_file:
            for line in pos_file:
                first, second = tuple(map(int, line.split()));
                if first >= len(self.nodeperm) or second >= len(self.nodeperm):
                    continue
                first_idx = self.nodeperm[first]
                first_word = self.graphdict[first_idx]
                second_idx = self.nodeperm[second]
                second_word = self.graphdict[second_idx]
                self.graph.add_edge(first_word, second_word)

    def tag(self, corpus):
        prev, prev2 = self.START
        tokens = []
        for sentence in corpus:
            context = self.START + [self._normalize(w) for w in sentence] + self.END
            for i, word in enumerate(sentence):
                tag = self.tagdict.get(word)
                if not tag:
                    features = self._get_features(i, word, context, prev, prev2)
                    tag = self.model.predict(features)
                tokens.append((word, tag))
                prev2 = prev
                prev = tag
        return tokens

    def train(self, sentences, save_loc=None, nr_iter=5):
        '''Train a model from sentences, and save it at ``save_loc``. ``nr_iter``
        controls the number of Perceptron training iterations.

        :param sentences: A list of (words, tags) tuples.
        :param save_loc: If not ``None``, saves a pickled model in this location.
        :param nr_iter: Number of training iterations.
        '''
        self._make_tagdict(sentences)
        self.model.classes = self.classes
        for iter_ in range(nr_iter):
            c = 0
            n = 0
            print "iteration: " ,iter_
            for tups in sentences:
                words = map(operator.itemgetter(0), tups)
                tags = map(operator.itemgetter(1), tups)
                prev, prev2 = self.START #do this complicatedly
                context = self.START + [self._normalize(w) for w in words] \
                                                                    + self.END
                for i, word in enumerate(words):
                    guess = self.tagdict.get(word)
                    if not guess:
                        #this is the operant part
                        feats = self._get_features(i, word, context, prev, prev2)
                        guess = self.model.predict(feats)
                        self.model.update(tags[i], guess, feats)
                    prev2 = prev
                    prev = guess
                    c += guess == tags[i]
                    n += 1
            random.shuffle(sentences)
        self.model.average_weights()
        # Pickle as a binary file
        if save_loc is not None:
            pickle.dump((self.model.weights, self.tagdict, self.classes),
                         open(save_loc, 'wb'), -1)
        return None

    def train_graph(self, sentences, save_loc=None, nr_iter=5):
        '''Train a model from graph, and save it at ``save_loc``. ``nr_iter``
        controls the number of Perceptron training iterations.

        :param sentences: A list of (words, tags) tuples.
        :param graph: a graph of the POSs which lead to each other.
        :param save_loc: If not ``None``, saves a pickled model in this location.
        :param nr_iter: Number of training iterations.
        '''
        self._make_tagdict(sentences)
        self.model.classes = self.classes
        for iter_ in range(nr_iter):
            c = 0
            n = 0
            print "iteration: " ,iter_
            for tups in sentences:
                if n % 1000 == 0:
                    print "n : ", n
                words = map(operator.itemgetter(0), tups)
                tags = map(operator.itemgetter(1), tups)
                context = self.START + [self._normalize(w) for w in words] \
                                                                    + self.END
                prev = self.START[0] #do this complicatedly
                for i, word in enumerate(words):
                    guess = self.tagdict.get(word)
                    if not guess:
                        #this is the operant part
                        feats = self._get_features_graph(i, word, context, prev, self.graph)
                        guess = self.model.predict(feats)
                        self.model.update(tags[i], guess, feats)
                    prev = guess
                    c += guess == tags[i]
                    n += 1
            random.shuffle(sentences)
        self.model.average_weights()
        # Pickle as a binary file
        if save_loc is not None:
            pickle.dump((self.model.weights, self.tagdict, self.classes),
                         open(save_loc, 'wb'), -1)
        return None

    def load(self, loc):
        '''Load a pickled model.'''
        try:
            w_td_c = pickle.load(open(loc, 'rb'))
        except IOError:
            msg = ("Missing trontagger.pickle file.")
            raise MissingCorpusError(msg)
        self.model.weights, self.tagdict, self.classes = w_td_c
        self.model.classes = self.classes
        return None

    def _normalize(self, word):
        '''Normalization used in pre-processing.

        - All words are lower cased
        - Digits in the range 1800-2100 are represented as !YEAR;
        - Other digits are represented as !DIGITS

        :rtype: str
        '''
        if '-' in word and word[0] != '-':
            return '!HYPHEN'
        elif word.isdigit() and len(word) == 4:
            return '!YEAR'
        elif word[0].isdigit():
            return '!DIGITS'
        else:
            return word.lower()

    def _get_features(self, i, word, context, prev, prev2):
        '''Map tokens into a feature representation, implemented as a
        {hashable: float} dict. If the features change, a new model must be
        trained.
        '''
        def add(name, *args):
            features[' '.join((name,) + tuple(args))] += 1

        i += len(self.START)
        features = defaultdict(int)
        # It's useful to have a constant feature, which acts sort of like a prior
        add('bias')
        add('i suffix', word[-3:])
        add('i pref1', word[0])
        add('i-1 tag', prev)
        return features

    def _get_features_graph(self, i, word, context, prev, graph):
        '''Map tokens into a feature representation, implemented as a
        {hashable: float} dict. If the features change, a new model must be
        trained.
        '''
        def add(name, *args):
            features[' '.join((name,) + tuple(args))] += 1

        i += len(self.START)
        features = defaultdict(int)
        # It's useful to have a constant feature, which acts sort of like a prior
        add('bias')
        add('i suffix', word[-3:])
        add('i pref1', word[0])
        #get the i-1 tag from the graph
        #therefore, the graph should be a digraph
        #see how that performance works
        add('i-1 tag', prev)
        for parent, _ in graph.in_edges([prev]):
            add('i-1 tag parent', parent)
        return features

    def _make_tagdict(self, sentences):
        '''Make a tag dictionary for single-tag words.'''
        counts = defaultdict(lambda: defaultdict(int))
        for sentence in sentences:
            for word, tag in sentence:
                counts[word][tag] += 1
                self.classes.add(tag)
        freq_thresh = 20
        ambiguity_thresh = 0.97
        for word, tag_freqs in counts.items():
            tag, mode = max(tag_freqs.items(), key=lambda item: item[1])
            n = sum(tag_freqs.values())
            # Don't add rare words to the tag dictionary
            # Only add quite unambiguous words
            if n >= freq_thresh and (float(mode) / n) >= ambiguity_thresh:
                self.tagdict[word] = tag


def _pc(n, d):
    return (float(n) / d) * 100

if __name__ == "__main__":
    pass
