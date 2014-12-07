from tagger import PerceptronTagger
from nltk.corpus import brown

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
    pass

if __name__ == "__main__":
    text = "Simple is better than complex. Complex is better than complicated."
    sentences = brown.tagged_sents()
    train, test = traintest_split(brown.tagged_sents())
    tagger= PerceptronTagger(load=False)
    tagger.train(train, nr_iter)
    stripped_tests = tag_strip(tests)
    tagger.test(tests, should be a validation set somewhere)
