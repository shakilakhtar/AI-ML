import os
from collections import defaultdict
from nltk.util import ngrams
from nltk import FreqDist
import math
''' Helper functions '''


def get_ngrams(data, n):
    """ function will extract n-grams on frequency defined """
    print("Doing", n, "gram Analysis: ")
    ngram_list = []
    ngram_data = ngrams(data, n)
    fd = FreqDist(ngram_data)
    print("number of unique words in ", n, "gram :", len(fd))
    print("number of common words in ", n, "gram :", len(fd.most_common()))
    print(" ")
    for key,value in fd.most_common(10):
        ngram_list.append(value)
    return ngram_list


def compute_idf(corpus):
    """function will compute inverse document frequency"""
    num_docs = len(corpus)
    idf = defaultdict(lambda: 0)
    for doc in corpus:
        for word in doc.keys():
            idf[word] += 1

    for word, value in idf.items():
        idf[word] = math.log(num_docs / value)
    return idf


def compute_weights(idf, doc):
    """function will compute weights"""
    for word, value in doc.items():
        doc[word] = idf[word] * (1 + math.log(value))


def build_inverted_index(idf, corpus):
    """function will build inverted indexes"""
    inverted_index = {}
    for word, value in idf.items():
        inverted_index[word] = {}
        inverted_index[word]['idf'] = value
        inverted_index[word]['postings_list'] = []

    for index, doc in enumerate(corpus):
        for word, value in doc.items():
            inverted_index[word]['postings_list'].append([index, value])

    return inverted_index
