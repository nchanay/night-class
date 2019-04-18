# Average numbers whose keys start with the same letter. Output a dictionary containing those letters as keys and the averages.
#
# d = {'a1':4, 'a2':2, 'a3':3, 'b1':10, 'b2':1, 'b3':1, 'c1':4, 'c2':5, 'c3':6}
# unify(d) -> {'a':3, 'b':4, 'c':5}


def unify(d):
    """
    >>> unify({'a1':4, 'a2':2, 'a3':3, 'b1':10, 'b2':1, 'b3':1, 'c1':4, 'c2':5, 'c3':6})
    {'a': 3, 'b': 4, 'c': 5}
    """
    # for key, item in d.items():
    #     new_dict[key[0]] = (new_dict.get(key[0], (0, 1)) + item)
    running_sum = {}
    for key, item in d.items():
        if key[0] in running_sum:
            current_sum, count = running_sum[key[0]]
            running_sum[key[0]] = (current_sum + item, count + 1)
        else:
            running_sum[key[0]] = (item, 1)
    return {key: round(rsum/count) for (key, (rsum, count)) in running_sum.items()}


d = {'a1':4, 'a2':2, 'a3':3, 'b1':10, 'b2':1, 'b3':1, 'c1':4, 'c2':5, 'c3':6}

print(unify(d))
