'''
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) 
of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).


Example 1:
    Input: s = "abc", t = "ahbgdc"
    Output: true
Example 2:
    Input: s = "axc", t = "ahbgdc"
    Output: false
'''

def isSubsequence(s, t):
    # If the length of s is greater than t, s cannot be a subsequence of t
    if len(s) > len(t):
        return False

    # If s is an empty string, it is a subsequence of any string
    if len(s) == 0:
        return True

    # Initialize a pointer for the current index in s
    current = 0
    
    # Iterate over each character in t
    for i in range(len(t)):
        # If we have matched all characters in s, we can stop
        if current >= len(s):
            break
        
        # If the current character in s matches the current character in t
        if s[current] == t[i]:
            # Move to the next character in s
            current += 1
    
    # If we have matched all characters in s, return True
    if current == len(s):
        return True
    
    # If not all characters in s were matched, return False
    return False

    
# Other implementation: 0ms runtime

def isSubsequence(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    if len(s) == len(t):
        if s == t:
            return True
        else:
            return False
    
    arr = list(s)
    
    if len(arr) == 0:
        return True
        
    for ele in list(t):
        if ele == arr[0]:
            arr.pop(0)
        if len(arr) == 0:
            return True
    
    return False

def isSubsequence(s: str, t: str) -> bool:
    i, j = 0, 0  # Initialize pointers for s and t

    while i < len(s) and j < len(t):
        if s[i] == t[j]:  # If characters match, move pointer i
            i += 1
        j += 1  # Always move pointer j

    return i == len(s)  # If i has reached the end of s, it's a subsequencedef isSubsequence(s: str, t: str) -> bool:
    i, j = 0, 0  # Initialize pointers for s and t

    while i < len(s) and j < len(t):
        if s[i] == t[j]:  # If characters match, move pointer i
            i += 1
        j += 1  # Always move pointer j

    return i == len(s)  # If i has reached the end of s, it's a subsequence