# Given a list of numbers, and a target number, find a pair of numbers from the list that sum to a target number
# Optional: return a list of all pairs of numbers that sum to a target value.

def find_pair(nums, target):
    """
    >>> find_pair([5, 6, 2, 3], 7)
    [5, 2]
    """
    # combos = []
    # for i in nums:
    #     for j in nums:
    #         if i == j:
    #             continue
    #         if i > j:
    #             break
    #         if i + j == target:
    #             combos.append([i, j])
    # return combos

    # combos = []
    # for i in range(len(nums)-1):
    #     for j in range(len(nums)-1, 0, -1):
    #         if i >= j:
    #             break
    #         if nums[i] + nums[j] == target:
    #             combos.append([nums[i] + nums[j]])
    # return combos

    # combos = []
    # for i in nums:
    #     if i < target:
    #         difference = target - i
    #         if difference in nums:
    #             combos.append([i, difference])
    #     return combos

    combos = []
    while len(nums) > 1:
        num = nums[-1]
        if num < target:
            difference = target - num
            if difference in nums:
                combos.append([num, difference])
        nums.pop()
    return combos


nums = [4, 3, 5, 2, 5, 2]
target = 7

print(find_pair(nums, target))
