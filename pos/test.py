from tagger import PerceptronTagger

if __name__ == "__main__":
    text = "Simple is better than complex. Complex is better than complicated."
    tagger= PerceptronTagger(load=False)
    tagger.train(sentences, nr_iter)
