def find_winner(votes):
    vote_count = {}
    
    for vote in votes:
        if vote in vote_count:
            vote_count[vote] += 1
        else:
            vote_count[vote] = 1
    max_votes=0
    winner=None
    for vote,count in vote_count.items():
        if count>max_votes:
            max_votes=count
            winner = vote

    return winner

votes=['a', 'b', 'a', 'c', 'a']
print("winners:",find_winner(votes))  
