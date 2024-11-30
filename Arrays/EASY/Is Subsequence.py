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
 

Constraints:

0 <= s.length <= 100
0 <= t.length <= 104
s and t consist only of lowercase English letters.

'''
class Solution(object):
    def isSubsequence(self, s, t):
       
        if len(s) > len(t):
            return False

        if len(s) == 0:
            return True

        current = 0
        for i in range(len(t)):
            if current >= len(s):
                break
            if s[current] == t[i]:
                current += 1
        
        if current == len(s):
            return True
        return False

# Other implementation: 0ms runtime

class Solution(object):
    def isSubsequence(self, s, t):
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
