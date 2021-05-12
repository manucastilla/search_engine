from se.query import parse_json_query, parse_raw_query
from se.retrieve import retrieve
from se.rank import rank_documents


def search(raw_query, index, docs):
    query = parse_raw_query(raw_query)
    # index_query = retrieve(index, query)
    print(query)
    json_q = parse_json_query(query)
    index_query = json_q.evaluate(index)
    print(json_q)
    ranked_index = rank_documents(raw_query, docs, index_query)
    return [docs[k] for k in ranked_index]
