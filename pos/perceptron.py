#inspired by sloria's perceptron implementation, which is nice and simple
from collections import defaultdict
import cPickle
import random

class AveragedPerceptron(object):
    def __init__(self):
        self.weights = {} #should be a dict of dicts
        self.classes = set()
        self._totals = defaultdict(int)
        self._tstamps = defaultdict(int)
        self.i #number instances

    def predict(self, features):
        scores = defaultdict(float)
        for feature, value in features.items():
            if feature not in self.weights or value == 0:
                continue
            for label, weight in self.weights[feature].items():
                scores[label] += value * weight
        #second member of tuple is for numerical stability
        return max(self.classes, key=lambda label: (scores[label], label))

    def update(self, truth, guess, features):
        pass

    def average_weights(self):
        pass

    def save(self, path):
        return pickle.dump(dict(self.weights), open(path, "w"))

    def load(self, path):
        self.weights = pickle.load(open(path))
        return None

#notice that this is not part of the class!
def train(nr_iter, examples):
    pass
