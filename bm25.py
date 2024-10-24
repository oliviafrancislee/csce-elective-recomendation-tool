import cleaning

def BM25(q):
    tracked_electives = cleaning.clean()
    tfs = cleaning.term_frequencies()
    lengths = cleaning.docLengths()
    avg_lengths = cleaning.totalAvgDocLen()
    query = cleaning.clean_query(q)

    titleweight  = 3
    bodyweight = 0.1
    btitle = 0.8
    bbody = 0.2
    k1 = 1.3

    for word in query {
        for 

                # length['title'] /= (1-titleweight) + (titleweight * (lengths.get(d).get(type) / avgLengths.get(type)))

    }


    #iterate through tfs
        #normalize tfs per zone (tfi): tf = tf / (1-b) + b * (lengths.get(d).get(type) / avgLengths.get(type))

