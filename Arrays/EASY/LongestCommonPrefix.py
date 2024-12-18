'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
'''

def LongestCommonPrefix(strs):
        # Initialize a variable to keep track of the minimum length of the strings
    minimum = float('inf')

    # Get the length of the shortest string in the list:
    for s in strs:
        # Update the minimum length if the current string is shorter
        if len(s) < minimum:
            minimum = len(s)

    # Initialize an index to track the current character position being compared
    index = 0

    # Loop until the index reaches the minimum length of the strings
    while index < minimum:
        # Iterate through each string in the list
        for s in strs:
            # Check if the character at the current index is the same for all strings
            if s[index] != strs[0][index]:
                # If a mismatch is found, return the common prefix up to the current index
                return s[:index]
        # Move to the next character index
        index += 1
            
    # If all characters up to the minimum length are the same, return the prefix
    return strs[0][:index]

def OtherSolution(strs):
    ans = ""
    strs = sorted(strs)
    first = strs[0]
    last = strs[-1]

    ''' 
    first is assigned the first string in the sorted list (strs[0]), 
    and last is assigned the last string (strs[-1]). These two strings
    are used to compare characters since they will have the most significant 
    differences in terms of prefixes.
    '''

    # Ensures that the loop does not exceed the length of either string.
    for i in range(min(len(first), len(last))):
        # Checks if the characters at the same index in first and last are the same.
        if first[i] != last[i]:
            # If they are not the same, it means the common prefix has ended.
            return ans
        # If the characters are the same, that character is appended to ans.
        ans += first[i]
    return ans

test1 = ["flower","flow","flight"]
test2 = ["dog","racecar","car"]

print(LongestCommonPrefix(test1))
print(LongestCommonPrefix(test2))

print(OtherSolution(test1))
print(OtherSolution(test2))
