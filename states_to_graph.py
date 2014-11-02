import cPickle
import itertools

def get_ngram(corpus, n):
    return itertools.izip(*[corpus[i:] for i in xrange(n)])

if __name__ == "__main__":
    states = []
    with open("brown_states.txt", "r") as states_file:
        states = cPickle.load(states_file)
    bigrs = get_ngram(states, 2)
    with open("brown_graph.txt", "w") as graph_file:
        for first, second in bigrs:
            graph_file.write("%d\t%d\n" % (first, second))
