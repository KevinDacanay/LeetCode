"""
A phrase is a palindrome if, after converting all uppercase letters into 
lowercase letters and removing all non-alphanumeric characters, it reads 
the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:
    Input: s = "A man, a plan, a canal: Panama"
    Output: true
    Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
    Input: s = "race a car"
    Output: false
    Explanation: "raceacar" is not a palindrome.

Example 3:
    Input: s = " "
    Output: true
    Explanation: s is an empty string "" after removing non-alphanumeric characters.
    Since an empty string reads the same forward and backward, it is a palindrome.
"""

def isPalindrome(s):
    # get rid of all non alphanumeric characters:
        word = ''.join([char for char in s if char.isalnum()])
        # get rid of capital letters
        word = word.lower()
        
        #initialize pointers
        left = 0
        right = len(word) - 1
        while left <= right:
            # keep going if each character matches
            if word[left] == word[right]:
                left += 1
                right -= 1
            # if mismatch, return False
            else:
                return False
        return True

s1 = "A man, a plan, a canal: Panama"
s2 = "race A car"
s3 = " "
print(isPalindrome(s1))
print(isPalindrome(s2))
print(isPalindrome(s3))