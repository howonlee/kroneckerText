from nltk.corpus import brown
import cPickle

if __name__ == "__main__":
    ls = [x for x in brown.words()]
    with open("brown.txt", "w") as brownfile:
        cPickle.dump(ls, brownfile)
