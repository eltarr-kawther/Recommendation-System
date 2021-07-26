def compute_score(book, m):
    v = vote_count.loc[book]
    R = vote_average.loc[book]
    
    score = (v/(v+m) * R) + (m/(m+v) * C)
    
    return score
