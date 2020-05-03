import os
import matplotlib.pyplot as plt
from operator import itemgetter
from utils import textprocessing, helpers

# file selected for analysis
file_location = os.path.join(os.getcwd(), 'resources/dataset/wiki_00')


def apply_zipfs_law(words):
    """function will verify zipfs law on frequency """
    fr = {}
    zipf_list = []
    for word in words:
        count = fr.get(word, 0)
        fr[word] = count + 1
    frequency = reversed(sorted(fr.items(), key=itemgetter(1)))

    for key,value in list(frequency):
        zipf_list.append(value)
    return zipf_list[:10]


def plot_graph(fd_data, n=None):
    """function will plot graph on frequency distribution data"""
    title = 'Word Count Distribution of ' + str(n) + '-gram, for first 10 common words'
    plt.plot(fd_data)
    plt.xlabel('Rank')
    plt.ylabel('Word Count')
    if n is not None:
        plt.title(title)
    else:
        plt.title('Zipfs Analysis - Word Count Distribution')
    plt.show()


# Part-1 of assignment doing corpus analysis
with open(file_location, encoding='utf-8') as file:
    file_content = file.read()

    # Normalizing the content
    text = textprocessing.normalize_text(file_content)
    # get tokens from normalized content
    tokens = textprocessing.get_tokens(text)
    # get unigrams
    fd_list = helpers.get_ngrams(tokens, 1)
    # plot unigram frequency distribution
    plot_graph(fd_list, 1)

    #  bigrams analysis and plotting
    fd_list = helpers.get_ngrams(tokens, 2)
    plot_graph(fd_list, 2)

    #  trigrams analysis and plotting
    fd_list = helpers.get_ngrams(tokens, 3)
    plot_graph(fd_list, 3)

    # Stem content
    stems = textprocessing.stem_words(tokens)
    # verify Zipf's law
    apply_zipfs_law(stems)

    # unigram analysis & plotting on stems
    fd_list = helpers.get_ngrams(stems, 1)
    plot_graph(fd_list, 1)

    # bigram analysis & plotting on stems
    fd_list = helpers.get_ngrams(stems, 2)
    plot_graph(fd_list, 2)

    # trigram analysis & plotting on stems
    fd_list = helpers.get_ngrams(stems, 3)
    plot_graph(fd_list, 3)

    # verify Zipf's law
    zipf_list = apply_zipfs_law(tokens)
    plot_graph(zipf_list)



