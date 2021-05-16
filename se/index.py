import json
from se.normalization import limpa_tudo
from collections import defaultdict


def make_index(docs):
    index = defaultdict(list)
    for k, doc in enumerate(docs):
        words = set(doc)
        #print(k, doc)
        for word in words:
            word = limpa_tudo(word)
            index[word].append(k)
    print(index)
    return index


def save_index(index, path):
    with open(path, 'w') as file:
        json.dump(index, file, indent=4)


def load_index(path):
    with open(path, 'r') as file:
        return json.load(file)
