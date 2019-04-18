# Write a function which takes a list as a parameter and returns a new list with any duplicates removed.
#
# def find_unique(nums):
#     ...
# nums = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]
# unique_nums = find_unique(nums) → [12, 24, 35, 88, 120, 155]


def find_unique(nums):
    """
    >>> find_unique([12, 24, 35, 24, 88, 120, 155, 88, 120, 155])
    [12, 24, 35, 88, 120, 155]
    """
    return sorted(list(set(nums)))


nums = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]
print(find_unique(nums))
