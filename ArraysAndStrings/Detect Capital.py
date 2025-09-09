"""
We define the usage of capitals in a word to be right when one 
of the following cases holds:
- All letters in this word are capitals, like "USA".
- All letters in this word are not capitals, like "leetcode".
- Only the first letter in this word is capital, like "Google".

Given a string word, return true if the usage of capitals in it is right. 

Example 1:
    Input: word = "USA"
    Output: true
Example 2:
    Input: word = "FlaG"
    Output: false
"""
def detect_capital(word):  
    # No Capital
    w1 = word.capitalize()
    if (word == w1):
        return True
    # All letters are capital:
    elif word.isupper():
        return True
    # All letters are lower:
    elif word.islower():
        return True

    return False

i1 = "USA"
i2 = "Google"
i3 = "leetcode"
i4 = "FlaG"
print(detect_capital(i1))
print(detect_capital(i2))
print(detect_capital(i3))
print(detect_capital(i4))