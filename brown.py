import nltk
import cPickle

if __name__ == "__main__":
    fileids = nltk.corpus.gutenberg.fileids()
    gutenberg_total = []
    for fileid in fileids:
        work = list(nltk.corpus.gutenberg.words(fileid))
        gutenberg_total += work
    with open("brown.txt", "w") as brown_file:
        cPickle.dump(gutenberg_total, brown_file)
