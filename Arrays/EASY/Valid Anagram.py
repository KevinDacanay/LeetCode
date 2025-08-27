"""
Given two strings s and t, return true if t is 
an anagram of s, and false otherwise.

Example 1:
    Input: s = "anagram", t = "nagaram"
    Output: true
Example 2:
    Input: s = "rat", t = "car"
    Output: false
"""
def is_anagram1(s, t):
    # edge case: s or t has more characters than the other
    if len(s) != len(t):
        return False

    # Create hashmaps to keep track of letters and their occurrences
    s_dict = {}
    t_dict = {}

    # Count the frequency of each character in both strings
    for char in s:
        s_dict[char] = s_dict.get(char, 0) + 1
    for char in t:
        t_dict[char] = t_dict.get(char, 0) + 1

    # Compare both dictionaries
    return s_dict == t_dict

def is_anagram2(s, t):
    if len(s) != len(t):
        return False

    s_dict = {}
    t_dict = {}
    for char in range(len(s)):
        if s[char] in s_dict:
            s_dict[s[char]] += 1
        else:
            s_dict[s[char]] = 1

        if t[char] in t_dict:
            t_dict[t[char]] += 1
        else:
            t_dict[t[char]] = 1
    if s_dict == t_dict:
        return True
    return False

s1 = "anagram"
t1 = "nagaram"
s2 = "car"
t2 = "rat"
print(is_anagram1(s1, t1))
print(is_anagram1(s2, t2))