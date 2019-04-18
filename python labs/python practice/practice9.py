# Write a function that merges two lists into a single list, where each element of the output list is a list containing two elements, one from each of the input lists.
#
# merge([5,2,1], [6,8,2]) → [[5,6],[2,8],[1,2]]

# Write a function combine_all that takes a list of lists, and returns a list containing each element from each of the lists.
#
# nums = [[5,2,3],[4,5,1],[7,6,3]]
# combine_all(nums) → [5,2,3,4,5,1,7,6,3]


def merge(list1, list2):
    # return [list(i) for i in zip(list1, list2)]
    # king_list = []
    # tuples = zip(list1, list2)
    # for i in tuples:
    #     king_list.append(list(i))
    # return king_list
    return [[list[i], list2[i]] for i in range(min(len(list1), len(list2))]


def combine_all(nums):
    return sum(nums, [])


list1 = [5, 2, 1]
list2 = [6, 8, 2]
print(merge(list1, list2))

nums = [[5, 2, 3], [6, 8, 2], [7, 6, 3]]
print(combine_all(nums))
