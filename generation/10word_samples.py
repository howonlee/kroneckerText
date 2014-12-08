import sys
import random

if __name__ == "__main__":
    assert len(sys.argv) > 2
    with open(sys.argv[1], "r") as sample_file:
        words = sample_file.read().split()
        for x in xrange(int(sys.argv[2])):
            random_start = random.randint(0, len(words) - 11)
            print " ".join(words[random_start:random_start+10])
