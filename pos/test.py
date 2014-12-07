from tagger import PerceptronTagger
from nltk.corpus import brown
import operator

def traintest_split(sentence_list):
    trains = []
    tests = []
    for idx, val in enumerate(sentence_list):
        if some hash: ##############
            trains.append(val)
        else:
            tests.append(val)
    return trains, tests

def tag_strip(sentence_list):
    #probably could do a double map, but meh
    new_sentence_list = []
    for sentence in sentence_list:
        new_sentence_list.append(map(operator.itemgetter(0), sentence))
    return new_sentence_list

def get_conf_mat(tags, test_tags, name="baseline"):
    assert len(tags) == len(test_tags)
    vocab = set()
    for tag in tags:
        vocab.add(tag)
    for tag in test_tags:
        vocab.add(test_tags)
    vocab_dict = turn the set into an index dict #############
    conf_mat = nonsparse array, hopefully not too high dim ##############
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
    tagger= PerceptronTagger(load=False)
    tagger.train(train, nr_iter)
    stripped_tests, corr_tags = tag_strip(tests)
    tags = tagger.tag(stripped_tests, tokenize=False)
    get_conf_mat(tags, test_tags)
