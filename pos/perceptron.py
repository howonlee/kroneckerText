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
        self.i = 0 #number instances

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
        def update_feature(c,f,w,v):
            param = (f,c)
            self._totals[param] += (self.i - self._tstamps[param]) * w
            self._tstamps[param] = self.i
            self.weights[f][c] = w + v
        self.i += 1
        if truth == guess:
            return None
        for f in features:
            weights = self.weights.setdefault(f, {})
            update_feature(truth, f, weights.get(truth, 0.0), 1.0)
            update_feature(guess, f, weights.get(guess, 0.0), -1.0)

    def average_weights(self):
        for feat, weights in self.weights.items():
            new_feat_weights = {}
            for clas, weight in weights.items():
                param = (feat, clas)
                total = self._totals[param]
                total += (self.i - self._tstamps[param]) * weight
                averaged = round(total / float(self.i), 3)
                if averaged:
                    new_feat_weights[clas] = averaged
            self.weights[feat] = new_feat_weights
        return None

    def save(self, path):
        return pickle.dump(dict(self.weights), open(path, "w"))

    def load(self, path):
        self.weights = pickle.load(open(path))
        return None

#notice that this is not part of the class!
def train(nr_iter, examples):
    model = AveragedPerceptron()
    for i in range(nr_iter):
        random_shuffle(examples)
        for features, class_ in examples:
            scores = model.predict(features)
            guess, score = max(scores.items(), key=lambda i: i[1])
            if guess != class_:
                model.update(class_, guess, features)
    model.average_weights()
    return model
