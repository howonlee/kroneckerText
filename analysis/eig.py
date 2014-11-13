import numpy as np
import scipy as sci
import scipy.sparse as sci_sparse
import collections
import matplotlib.pyplot as plt
from nltk.corpus import brown

words = brown.words()[:20000]
index_set = set()
for word in words:
    index_set.add(word)
index_list = list(index_set)
index_len = len(index_list)
print index_len
index = {}
for idx, word in enumerate(index_list):
    index[word] = idx
word_arr = sci_sparse.dok_matrix((index_len, index_len))
for word, prevword in zip(words, words[1:]):
    word_arr[index[prevword], index[word]] += 1
U, S, V = sci_sparse.linalg.svds(word_arr, k=index_len-1)
eigvals = S**2 / np.cumsum(S)[-1]
print eigvals.shape

fig = plt.figure()
sing_vals = np.arange(index_len) + 1
print sing_vals.shape
plt.plot(sing_vals, eigvals, 'ro-', linewidth=2)
plt.yscale('log')
plt.xscale('log')
plt.title('Scree Plot')
plt.xlabel('Principal Component')
plt.ylabel('Eigenvalue')
plt.show()
