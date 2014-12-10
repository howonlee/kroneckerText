import csv
import collections

if __name__ == "__main__":
    cts = collections.Counter()
    with open("res.csv") as res_file:
        res = csv.reader(res_file, delimiter=",", quotechar='"')
        for row in res:
            cts[row[5]] += 1
            cts[row[7]] += 1
    print cts
