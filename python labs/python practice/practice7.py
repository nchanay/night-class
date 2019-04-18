# Write a function to combine two lists of equal length into one, alternating elements.

# combine(['a','b','c'],[1,2,3]) → ['a', 1, 'b', 2, 'c', 3]


def combine(nums1, nums2):
    """
    returns list of list1 and list2 elements alternating

    >>> combine(['a','b','c'],[1,2,3])
    ['a', 1, 'b', 2, 'c', 3]
    """
    return sum([list(i) for i in zip(nums1, nums2)], [])
    # test = []
    # tuples = zip(nums1, nums2)
    # for i in tuples:
    #     test.append(list(i))
    # return sum(test, [])


nums1 = ['a', 'b', 'c']
nums2 = [1, 2, 3]

print(combine(nums1, nums2))
