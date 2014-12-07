from tagger import PerceptronTagger
from nltk.corpus import brown
import operator
import itertools
import numpy as np

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

def get_conf_mat(tags, test_tags, name="baseline"):
    assert len(tags) == len(test_tags)
    vocab = set()
    for tag in tags:
        vocab.add(tag)
    for tag in test_tags:
        vocab.add(test_tags)
    curr_idx = 0
    vocab_dict = {}
    for word in vocab:
        vocab_dict[word] = curr_idx
        curr_idx += 1
    conf_mat = np.zeros((curr_idx, curr_idx))
    for idx, tup in enumerate(zip(tags, test_tags)):
        tag, test = tup
        conf_mat[vocab_dict[tag], vocab_dict[test]] += 1
    plt.matshow(conf_mat)
    plt.colorbar()
    plt.savefig(name + "_conf_mat")

if __name__ == "__main__":
    text = "Simple is better than complex. Complex is better than complicated."
    sentences = brown.tagged_sents()
    train, test = traintest_split(brown.tagged_sents())
    tagger= PerceptronTagger(load=True)
    #tagger.train(train, "baseline_res")
    stripped_tests, test_tags = tag_strip(test)
    tags = tagger.tag(stripped_tests, tokenize=False)
    print tags
    print "==========="
    test_tags = list(itertools.chain.from_iterable(test_tags))
    get_conf_mat(tags, test_tags)
