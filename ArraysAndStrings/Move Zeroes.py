"""
Given an integer array nums, move all 0's to the end of it 
while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.

Example 1:
    Input: nums = [0,1,0,3,12]
    Output: [1,3,12,0,0]

Example 2:
    Input: nums = [0]
    Output: [0]
"""
def move_zeroes1(nums):
    for n in nums:
        if n == 0:
            nums.remove(0)
            nums.append(0)

def move_zeroes2(nums):
    i = 0
    for j in range(len(nums)):
        # if number is a non-zero, slide it forward to nums[i]
        if nums[j] != 0:
            nums[i] = nums[j]
            i += 1
    # after iterating through nums, i is now equal to the index where zeroes should start at
    while i < len(nums):
        nums[i] = 0
        i += 1