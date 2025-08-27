"""
Given an integer array nums and an integer k, return 
true if there are two distinct indices i and j in the 
array such that nums[i] == nums[j] and abs(i - j) <= k.

Example 1:
    Input: nums = [1,2,3,1], k = 3
    Output: true
Example 2:
    Input: nums = [1,0,1,1], k = 1
    Output: true
Example 3:
    Input: nums = [1,2,3,1,2,3], k = 2
    Output: false
"""
def contains_duplicate(nums, k):
    i = 0
    seen = dict()

    for i in range(len(nums)):
        # print(seen)
        if nums[i] in seen:
            # print(nums[i])
            # # print(((seen.get(nums[i]) - i)))
            # print(seen.get(nums[i]))
            if abs(seen.get(nums[i]) - i) <= k:
                return True
        seen[nums[i]] = i
    return False

n1 = [1,2,3,1]
k1 = 3
n2 = [1,0,1,1]
k2 = 1
n3 = [1,2,3,1,2,3]
k3 = 2
print(contains_duplicate(n1, k1))
print(contains_duplicate(n2, k2))
print(contains_duplicate(n3, k3))