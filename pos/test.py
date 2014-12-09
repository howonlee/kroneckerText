from tagger import PerceptronTagger
from nltk.corpus import brown
import operator
import itertools
import sys
import numpy as np
import matplotlib.pyplot as plt

def traintest_split(sentence_list):
    trains = []
    tests = []
    for idx, val in enumerate(sentence_list):
        if idx % 3 == 1 or idx % 3 == 2: ### maybe some kind of bias?
            trains.append(val)
        else:
            tests.append(val)
    return trains, tests

def tag_strip(sentence_list):
    #probably could do a double map, but meh
    new_sentence_list = []
    tags_list = []
    for sentence in sentence_list:
        new_sentence_list.append(map(operator.itemgetter(0), sentence))
        tags_list.append(map(operator.itemgetter(1), sentence))
    return new_sentence_list, tags_list

def get_conf_mat(tags, test_tags, name="gen_res"):
    tags = map(operator.itemgetter(1), tags)
    #test_tags = map(operator.itemgetter(1), tags)
    assert len(tags) == len(test_tags)
    vocab = set()
    for tag in tags:
        vocab.add(tag)
    for tag in test_tags:
        vocab.add(tag)
    curr_idx = 0
    vocab_dict = {}
    for word in vocab:
        vocab_dict[word] = curr_idx
        curr_idx += 1
    conf_mat = np.zeros((curr_idx, curr_idx))
    for idx, tup in enumerate(zip(tags, test_tags)):
        tag, test = tup
        conf_mat[vocab_dict[tag], vocab_dict[test]] += 1
    np.save(name + "_conf_mat", conf_mat)
    plt.matshow(conf_mat)
    plt.colorbar()
    plt.savefig(name + "_conf_mat")

if __name__ == "__main__":
    assert len(sys.argv) >  1
    sentences = brown.tagged_sents()
    train, test = traintest_split(brown.tagged_sents())
    stripped_tests, test_tags = tag_strip(test)
    #must put actual filename
    if sys.argv[1] == "gen_res":
        tagger= PerceptronTagger(load=None)
        tagger.train(train, sys.argv[1])
        #tag or tag_graph
        tags = tagger.tag(stripped_tests)
    elif sys.argv[1] == "bigram":
        tagger= PerceptronTagger(load=None)
        tagger.train_ngram(train, sys.argv[1])
        #tag or tag_graph
        tags = tagger.tag_ngram(stripped_tests)
    elif sys.argv[1] == "kron":
        tagger= PerceptronTagger(load=None)
        tagger.train_graph(train, sys.argv[1])
        #tag or tag_graph
        tags = tagger.tag_graph(stripped_tests)
    test_tags = list(itertools.chain.from_iterable(test_tags))
    get_conf_mat(tags, test_tags, sys.argv[1])
