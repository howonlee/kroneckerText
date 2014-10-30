import cPickle

def find_ngrams(input_list, n):
    return zip(*[input_list[i:] for i in range(n)])

if __name__ == "__main__":
    gutenberg_total = []
    with open("../brown.txt", "r") as brown_file:
        gutenberg_total = cPickle.load(brown_file)
    tris = find_ngrams(gutenberg_total, 3)
