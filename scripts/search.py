#!/usr/bin/env python3
# python scripts/search.py data/bolsonaro_tweets.json data/index.json
from argparse import ArgumentParser

from se.archive import load_archive
from se.index import load_index
from se.search import search
from se.normalization import limpa_tudo


MSG_DESCRIPTION = 'Busca.'


def main():
    parser = ArgumentParser(description=MSG_DESCRIPTION)
    parser.add_argument('filename_docs', help='Os doc.')
    parser.add_argument('filename_index', help='Os indice.')
    parser.add_argument('query', nargs='+', help='A query.')
    args = parser.parse_args()

    docs = load_archive(args.filename_docs)
    index = load_index(args.filename_index)

    query_limpa = list(map(limpa_tudo, args.query))

    query = " ".join(query_limpa)
    docs_searched = search(query, index, docs)

    for doc in docs_searched:
        print(" ".join(doc))
        print('=' * 80)

    if len(docs_searched) == 0:
        print("Esta palavra não existe no conjunto de tweets")


if __name__ == '__main__':
    main()
