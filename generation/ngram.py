import cPickle

def find_ngrams(input_list, n):
    return zip(*[input_list[i:] for i in range(n)])

if __name__ == "__main__":
    brown_total = []
    with open("../brown_states.txt", "r") as brown_file:
        brown_total = cPickle.load(brown_file)
    bis = find_ngrams(brown_total, 2)
    #make the matrix
    #sample from the matrix
    #print the sample
    #next step: turn the sample back into words, see that they're all bigram-ish
