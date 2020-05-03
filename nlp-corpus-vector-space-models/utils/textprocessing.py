import re
from nltk.stem.porter import PorterStemmer
from nltk import word_tokenize
''' Text processing '''


def normalize_text(data):
    """function will do text cleaning e.g. removing html tags"""
    clean_text = re.sub('[^A-Za-z]+', ' ', data)
    only_a = ""
    for word in clean_text.split():
        if ((word.isalpha() is False) & (word.isdigit() is True)) | ((word.isalpha() is True) & (word.isdigit() is False)):
            only_a += (word+" ")
    return only_a


def get_tokens(text):
    """function will tokenize text into words"""
    print(" ")
    print("-------- Tokenizing -------")
    tokens = word_tokenize(text)
    return tokens


def stem_words(tokens):
    """function will apply stemming on tokens"""
    print(" ")
    print("-------- Stemming -------")
    stemmer = PorterStemmer()
    stems = []
    for w in tokens:
        stems.append(stemmer.stem(w))
    return stems


def preprocess_text(text):
    processed_text = get_tokens(text.lower())
    stemmed_words = stem_words(processed_text)
    return stemmed_words

