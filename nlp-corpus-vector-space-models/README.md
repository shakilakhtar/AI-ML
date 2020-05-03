# NLP models using NLTK python library

## Code 
Code has one single module and textprocessing, helper functions reusable code. Functions are commented with their usage purpose.
Wikipedia data file 'wiki_00' is used in the analysis. Dataset file is copied in resources/dataset directory

## Corpus Analysis

Run `corpus_analysis.py` as python script. The script will plot the graph and print ngram analysis on console

```bash
$ pyhton corpus_analysis.py
```

## Vector Space Based Model

Run `vector_space_model.py` script to index documents stored in `resources/dataset` directory:

```bash
$ python vector_space_model.py
```

The indexed data is stored in `data/` directory. The set of words is stored in `dictionary.txt` file.
The list of all documents and inverted index is serialized into `docs.pickle` and `inverted_index.pickle` files (using `pickle` serializer module). These files will be read by `query.py` script to perform query.

To perform query, run `query.py` script and provide an argument for it:

```bash
$ python query.py "your query here"
```