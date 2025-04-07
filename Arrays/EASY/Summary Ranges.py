'''
You are given a sorted unique integer array nums.

A range [a,b] is the set of all integers from a to b (inclusive).

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. 
That is, each element of nums is covered by exactly one of the ranges, and there is 
no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:
    "a->b" if a != b
    "a" if a == b

Example 1:
    Input: nums = [0,1,2,4,5,7]
    Output: ["0->2","4->5","7"]
    Explanation: The ranges are:
    [0,2] --> "0->2"
    [4,5] --> "4->5"
    [7,7] --> "7"
    
Example 2:
    Input: nums = [0,2,3,4,6,8,9]
    Output: ["0","2->4","6","8->9"]
    Explanation: The ranges are:
    [0,0] --> "0"
    [2,4] --> "2->4"
    [6,6] --> "6"
    [8,9] --> "8->9"
'''
def summary_ranges(nums):
    # Initialize index and result list
    i = 0
    ranges = []

    # Iterate through the input list
    while i < len(nums):
        # Mark the start of a new range
        start = nums[i]
        
        # Check for consecutive numbers
        while i < len(nums) - 1 and nums[i] + 1 == nums[i + 1]:
            # Move to the next number
            i += 1

        # If the range consists of only one number, append it as a string
        if start != nums[i]:
            # Append the range as a string in the format "start->end"
            ranges.append(f"{start}->{nums[i]}")
        else:
            # Append the single number as a string
            ranges.append(str(start))
        
        # Move to the next number
        i += 1
    
    # Return the list of ranges
    return ranges

# Test cases
print(summary_ranges([0, 2, 3, 4, 6, 8, 9]))  # Output: ["0", "2->4", "6", "8->9"]
print(summary_ranges([0, 1, 2, 4, 5, 7]))  # Output: ["0->2", "4->5", "7"]
print(summary_ranges([0]))  # Output: ["0"]
print(summary_ranges([]))  # Output: []
print(summary_ranges([1, 2, 3, 4, 5]))  # Output: ["1->5"]
print(summary_ranges([1, 3, 5, 7, 9]))  # Output: ["1", "3", "5", "7", "9"]