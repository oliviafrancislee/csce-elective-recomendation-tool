import data as cleaning
import math

def BM25(q):
    tracked_electives = cleaning.clean()
    tfs = cleaning.term_frequencies(tracked_electives)[0]
    dfs = cleaning.term_frequencies(tracked_electives)[1]
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
            if word in tfs[doc]['title'].keys():
                tftitle = (tfs[doc]['title'][word]) / (1-btitle) + (btitle * (lengths[doc]['title'] / avg_lengths['title']))
                    
            else:
                tftitle = 0

            if word in tfs[doc]['body'].keys():
                tfbody = (tfs[doc]['body'][word]) / (1-bbody) + (bbody * (lengths[doc]['body'] / avg_lengths['body']))

            else:
                tfbody = 0

            tfnormalized = titleweight * tftitle + bodyweight * tfbody
            
            if word in dfs.keys():
                bm25 += math.log(len(tfs) / len(dfs[word])) * ((k1 + 1) * tfnormalized) / (k1 + tfnormalized)
        
        bm25dict[doc] = bm25  
        
    bm25ranking = sorted(bm25dict, key = bm25dict.get, reverse = True)
    tracks_bm25ranking = {}
    for track in tracked_electives.keys():
        tracks_bm25ranking[track] = {}
        for elective in bm25ranking:
            if elective in tracked_electives[track].keys():
                class_info = {}
                class_info['score'] = bm25dict[elective]
                class_info['desc'] = tracked_electives[track][elective]
                tracks_bm25ranking[track][elective] = class_info

    return tracks_bm25ranking