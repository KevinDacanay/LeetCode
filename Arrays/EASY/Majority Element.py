"""
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than 
⌊n / 2⌋ times. You may assume that the majority element always 
exists in the array.

Example 1:
    Input: nums = [3,2,3]
    Output: 3
Example 2:
    Input: nums = [2,2,1,1,1,2,2]
    Output: 2
"""
def majority_element(nums):
    
    majority = len(nums) // 2
    seen = dict()
    for n in nums:
        if n in seen:
            seen[n] += 1
        else:
            seen[n] = 1
        if seen.get(n) > majority:
            return n
    return 0

n1 = [2,2,1,1,1,2,2]
n2 = [3,2,3]
print(majority_element(n1))
print(majority_element(n2))