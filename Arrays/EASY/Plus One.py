"""
You are given a large integer represented as an integer 
array digits, where each digits[i] is the ith digit of the 
integer. The digits are ordered from most significant to 
least significant in left-to-right order. The large integer 
does not contain any leading 0's.

Increment the large integer by one and return the resulting 
array of digits.
 
Example 1:
    Input: digits = [1,2,3]
    Output: [1,2,4]
    Explanation: The array represents the integer 123.
    Incrementing by one gives 123 + 1 = 124.
    Thus, the result should be [1,2,4].

Example 2:
    Input: digits = [4,3,2,1]
    Output: [4,3,2,2]
    Explanation: The array represents the integer 4321.
    Incrementing by one gives 4321 + 1 = 4322.
    Thus, the result should be [4,3,2,2].

Example 3:
    Input: digits = [9]
    Output: [1,0]
    Explanation: The array represents the integer 9.
    Incrementing by one gives 9 + 1 = 10.
    Thus, the result should be [1,0].
"""
def plus_one1(digits):
    # create a string of the given integer array
    num_str = ''.join(map(str, digits))
    # turn it into an integer and incerement by 1
    num_int = int(num_str) + 1
    # return a list of integers
    return [int(num) for num in str(num_int)]

def plus_one2(digits):
    sum = ""
    l = []
    for i in range(len(digits)):
        sum += str(digits[i])
    sum = int(sum) + 1
    sum = str(sum)
    for i in range(len(str(sum))):
        l.append(int(sum[i]))
    return l

d1 = [1,2,3]
d2 = [4,3,2,1]
d3 = [9]
print(plus_one1(d1))
print(plus_one1(d2))
print(plus_one1(d3))
print(plus_one2(d1))
print(plus_one2(d2))
print(plus_one2(d3))