import numpy as np
import sys

if __name__ == "__main__":
    assert len(sys.argv) > 1
    confmat = np.load(sys.argv[1])
    print confmat.trace() / confmat.sum()
