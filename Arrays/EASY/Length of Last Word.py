"""
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.

 

Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
Example 3:

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.
"""
def length_of_last_word(s):
    word = s.strip()
    word = word.split(" ")
    return len(word[-1])

s1 = "Hello World" 
s2 = "  fly me  to  the moon   " 
s3 = "luffy is  still  joyboy"
print(length_of_last_word(s1)) 
print(length_of_last_word(s2)) 
print(length_of_last_word(s3)) 

