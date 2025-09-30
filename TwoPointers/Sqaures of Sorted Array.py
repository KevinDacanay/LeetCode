"""
Given an integer array nums sorted in non-decreasing order, 
return an array of the squares of each number sorted in non-decreasing order.
 
Example 1:
    Input: nums = [-4,-1,0,3,10]
    Output: [0,1,9,16,100]
    Explanation: After squaring, the array becomes [16,1,0,9,100].
    After sorting, it becomes [0,1,9,16,100].
Example 2:
    Input: nums = [-7,-3,2,3,11]
    Output: [4,9,9,49,121]
"""
def sorted_squares1(nums):
    arr = []
    for i in nums:
        arr.append(i * i)
    arr.sort()

    return arr

def sorted_squares2(nums):
    arr = sorted([num ** 2 for num in nums])
    return arr

n1 = [-4,-1,0,3,10]
n2 = [-7,-3,2,3,11]
print(sorted_squares1(n1))
print(sorted_squares2(n2))
print(sorted_squares1(n1))
print(sorted_squares2(n2))