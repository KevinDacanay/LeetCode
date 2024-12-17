'''
Given an integer array nums of size n, return the number with the value closest to 0 in nums. 
If there are multiple answers, return the number with the largest value.


Example 1:

Input: nums = [-4,-2,1,4,8]
Output: 1
Explanation:
The distance from -4 to 0 is |-4| = 4.
The distance from -2 to 0 is |-2| = 2.
The distance from 1 to 0 is |1| = 1.
The distance from 4 to 0 is |4| = 4.
The distance from 8 to 0 is |8| = 8.
Thus, the closest number to 0 in the array is 1.
Example 2:

Input: nums = [2,-1,1]
Output: 1
Explanation: 1 and -1 are both the closest numbers to 0, so 1 being larger is returned.
 

Constraints:

1 <= n <= 1000
-105 <= nums[i] <= 105
'''

def findClosestNumber(nums):
    
    # Initialize minimum to be a big number "infinity"
    minimum = float('inf')

    # Iterate through each number in nums
    for i in nums:
        # Set variable 'a' to be the absolute value of the minimum
        a = abs(minimum)
        # Check if the absolute value of i is less than a:
        if abs(i) < a:
            # If it is, update the minimum to be i
            minimum = i
        # If the absolute value of i is equal to a:
        elif i == a:
            # If i is greater than the current minimum, update the minimum to be i
            if i > minimum: 
                minimum = i
    # Return the minimum
    return minimum
