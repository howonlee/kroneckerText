import re

def no_commas(line):
    return re.sub('[^0-9a-zA-Z ]+', '', line)

if __name__ == "__main__":
    snippets_1 = []
    snippets_2 = []
    snippets_3 = []
    with open("genned_snippets", "r") as file1:
        snippets_1 = map(no_commas, file1.readlines())
    with open("unigram_genned_snippets", "r") as file2:
        snippets_2 = map(no_commas, file2.readlines())
    with open("ngram_genned_snippets", "r") as file3:
        snippets_3 = map(no_commas, file3.readlines())
    for first, second, third in zip(snippets_1, snippets_2, snippets_3):
        print first, ",", second, ",", third
