# Problem 6
# Write a function to move all the elements of a list with value less than 10 to a new list and return it.
#
# def extract_less_than_ten(nums):
#
# Problem 7
# Write a function to find all common elements between two lists.
#
# def common_elements(nums1, nums2):

def extract_less_than_ten(nums):
    return [i for i in nums if i < 10]

nums = [1, 10, 2, 20, 3, 30, 4, 40, 5, 50]
print(extract_less_than_ten(nums))

def common_elements(nums1, nums2):
    # return [i for i in nums1 if i in nums2]
    return list(set(nums1) & set(nums2))

nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nums2 = [11, 2, 33, 4, 55, 6, 77, 8, 99, 10]

print(common_elements(nums1, nums2))
