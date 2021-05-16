import math


def score_document(terms, doc, index_query, index):
    score = 0
    for word in terms:
        f = 0
        for docword in set(doc):
            if word == docword:
                f += 1
        score += math.log(1+f, 2)*math.log(len(index)/len(index[word]), 2)
    return score


def rank_documents(query, docs, index_query, index):
    ranked_index = []
    terms = query.get_terms()
    for doc_number in index_query:
        doc = docs[doc_number]
        score = score_document(terms, doc, index_query, index)
        ranked_index.append((score, doc_number))
    ranked_index = sorted(ranked_index, key=lambda x: -x[0])
    return [item[1] for item in ranked_index]
