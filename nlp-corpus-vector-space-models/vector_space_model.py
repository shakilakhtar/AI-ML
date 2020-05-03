import os
import sys
import pickle
from collections import Counter
from utils import textprocessing, helpers
''' vector-space based information retrieval system '''

print('Indexing....')

resources_path = os.path.join(os.getcwd(), 'resources')
data_path = os.path.join(os.getcwd(), 'data')

if not os.path.isdir(resources_path):
    print('ERROR: The {} is not a directory or does not exist'.format(
        resources_path))
    sys.exit(1)

if not os.path.exists(data_path):
    os.mkdir(data_path)

# Get dataset
dataset_path = os.path.join(resources_path, 'dataset')
file_name='wiki_00'
doc = os.path.join(os.getcwd(), dataset_path+'/'+file_name)

corpus = []
with open(doc, encoding='utf-8') as f:
    text = f.read()
    words = textprocessing.preprocess_text(text)
    bag_of_words = Counter(words)
    corpus.append(bag_of_words)

idf = helpers.compute_idf(corpus)
for doc in corpus:
    helpers.compute_weights(idf, doc)

inverted_index = helpers.build_inverted_index(idf, corpus)

docs_file = os.path.join(data_path, 'docs.pickle')
inverted_index_file = os.path.join(data_path, 'inverted_index.pickle')
dictionary_file = os.path.join(data_path, 'dictionary.txt')

# Serialize data
with open(docs_file, 'wb') as f:
    pickle.dump(doc, f)

with open(inverted_index_file, 'wb') as f:
    pickle.dump(inverted_index, f)

with open(dictionary_file, 'w') as f:
    for word in idf.keys():
        f.write(word + '\n')

print('Index done.')
