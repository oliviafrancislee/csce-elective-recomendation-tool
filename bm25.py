import cleaning

tracked_electives = cleaning.clean()

def BM25(tracked_electives, query):
    titleweight  = 3
    bodyweight = 0.1

    btitle = 0.8
    bbody = 0.2

    k1 = 1.3
