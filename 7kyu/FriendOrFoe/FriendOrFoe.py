def friend(x):
    res = []
    for friend in x:
        if len(friend) == 4:
            res.append(friend)
    return res
