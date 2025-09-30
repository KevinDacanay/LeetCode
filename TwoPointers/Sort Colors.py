"""
Given an array nums with n objects colored red, white, or blue, sort them 
in-place so that objects of the same color are adjacent, with the colors 
in the order red, white, and blue.
We will use the integers 0, 1, and 2 to represent the color red, white, 
and blue, respectively.
You must solve this problem without using the library's sort function.

Example 1:
    Input: nums = [2,0,2,1,1,0]
    Output: [0,0,1,1,2,2]
Example 2:
    Input: nums = [2,0,1]
    Output: [0,1,2]
"""
def sort_colors1(nums):
    max_val = max(nums)
    count_arr = [0] * (max_val + 1)

    while len(nums) > 0:
        num = nums.pop(0)
        count_arr[num] += 1
    
    for i in range(len(count_arr)):
        while count_arr[i] > 0:
            nums.append(i)
            count_arr[i] -= 1
    
    return nums

def sort_colors2(nums):
    count_0 = 0
    count_1 = 0
    count_2 = 0

    for n in nums:
        if n == 0: count_0 += 1
        elif n == 1: count_1 += 1
        else: count_2 += 1

    index = 0
    for _ in range(count_0):
        nums[index] = 0
        index += 1

    for _ in range(count_1):
        nums[index] = 1
        index += 1
        
    for _ in range(count_2):
        nums[index] = 2
        index += 1 
    return nums

def sort_colors3(nums):
    low = 0
    mid = 0
    high = len(nums) - 1

    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            mid += 1
            low += 1
        elif nums[mid] == 2:
            nums[high], nums[mid] = nums[mid], nums[high]
            high -= 1
        else: 
            mid += 1
    return nums
n1 = [2,0,2,1,1,0]
n2 = [2,0,1]
n3 = [0,0,0,0,1,2,1,2,1,2,0,1,1,1,2]

print(sort_colors1(n1))
print(sort_colors1(n2))
# print(sort_colors1(n3))
print(sort_colors2(n1))
print(sort_colors2(n2))
print(sort_colors2(n3))
print(sort_colors3(n1))
print(sort_colors3(n3))
print(sort_colors3(n2))