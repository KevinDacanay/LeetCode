"""
Given an input string s, reverse the order of the words.
A word is defined as a sequence of non-space characters.
The words in s will be separated by at least one space.
Return a string of the words in reverse order concatenated by a single space.
Note that s may contain leading or trailing spaces or 
multiple spaces between two words. The returned string 
should only have a single space separating the words. 
Do not include any extra spaces.

Example 1:
    Input: s = "the sky is blue"
    Output: "blue is sky the"
Example 2:
    Input: s = "  hello world  "
    Output: "world hello"
    Explanation: Your reversed string should not contain leading or trailing spaces.
Example 3:
    Input: s = "a good   example"
    Output: "example good a"
    Explanation: You need to reduce multiple spaces between two words to a single 
    space in the reversed string
"""
def reverse_string(s):
    s = s.split()
    left = 0
    right = len(s) - 1

    while left <= right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

    return " ".join(s)

s1 = "the sky is blue"
s2 = "  hello world  "
s3 = "a good      example"
print(reverse_string(s1))
print(reverse_string(s2))
print(reverse_string(s3))