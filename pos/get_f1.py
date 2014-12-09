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
    print "========="
    print sys.argv[1]
    precisions = []
    recalls = []
    f1s = []
    for x in xrange(confmat.shape[0]):
        precision = float(confmat[x,x]) / confmat.sum(0)[x]
        recall = float(confmat[x,x]) / confmat.sum(1)[x]
        precisions.append(precision)
        recalls.append(recall)
        f1s.append(2 * precision * recall / (precision + recall))
    processed_f1s = process(f1s)
    processed_precision = process(precisions)
    processed_recall = process(recalls)
    print "f1: ", sum(processed_f1s) / len(processed_f1s)
    print "precision: ", sum(processed_precision) / len(processed_precision)
    print "recall: ", sum(processed_recall) / len(processed_recall)
