import cleaning
import math

def BM25(q):
    tracked_electives = cleaning.clean()
    tfs = cleaning.term_frequencies()[0]
    dfs = cleaning.term_frequencies()[1]
    lengths = cleaning.docLengths()
    avg_lengths = cleaning.totalAvgDocLen()
    query = cleaning.clean_query(q)

    titleweight  = 3
    bodyweight = 0.1
    btitle = 0.8
    bbody = 0.2
    k1 = 1.3

    bm25dict = {} #dictionary to store the bm25 scores for each document
    for doc in tfs.keys():
        bm25 = 0
        for word in query:
            tftitle = (tfs[doc]['title'][word]) / (1-btitle) + (btitle * (lengths[doc]['title'] / avg_lengths['title']))
            tfbody = (tfs[doc]['body'][word]) / (1-bbody) + (bbody * (lengths[doc]['body'] / avg_lengths['body']))

            tfnormalized = titleweight * tftitle + bodyweight * tfbody
            bm25 += math.log((len(tracked_electives)) / len(dfs[word])) * ((k1 + 1) * tfnormalized) / (k1 + tfnormalized)
        
        bm25dict[doc] = bm25  

    return sorted(bm25dict, key = bm25dict.get, reverse = True) 


#Make function that calls BM25 and returns the top X results in each track 