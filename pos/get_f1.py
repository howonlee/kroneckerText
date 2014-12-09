import numpy as np
import sys
import math

def process(arr):
    processed = []
    for member in arr:
        if math.isnan(member):
            processed.append(0)
        else:
            processed.append(member)
    return processed

if __name__ == "__main__":
    assert len(sys.argv) > 1
    confmat = np.load(sys.argv[1])
    precisions = []
    recalls = []
    f1s = []
    for x in xrange(confmat.shape[0]):
        precision = float(confmat[x,x]) / confmat.sum(0)[x]
        recall = float(confmat[x,x]) / confmat.sum(1)[x]
        precisions.append(precision)
        recalls.append(recall)
        f1s.append(2 * precision * recall / (precision + recall))
    print "precisions: ", precisions
    print "recalls: ", recalls
    print "f1s: ", f1s #there's a lot of POS tags that don't matter
    processed_f1s = process(f1s)
    processed_precision = process(precisions)
    processed_recall = process(recalls)
    print sum(processed_f1s) / len(processed_f1s)
    print sum(processed_precision) / len(processed_precision)
    print sum(processed_recall) / len(processed_recall)
