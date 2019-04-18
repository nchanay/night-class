# Problem 6
# Return the number of letter occurances in a string.

def count_letter(letter, word):
    """
    >>> count_letter('i', 'antidisestablishmentterianism')
    5
    """
    # count = 0
    # for i in word:
    #     if i == letter:
    #         count += 1
    # return count
    return len([i for i in word if i == letter])

# count_letter('i', 'antidisestablishmentterianism') → 5
# count_letter('p', 'pneumonoultramicroscopicsilicovolcanoconiosis') → 2

print(count_letter('i', 'antidisestablishmentterianism'))
