"""
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between 
a letter in pattern and a non-empty word in s. Specifically:

Each letter in pattern maps to exactly one unique word in s.
Each unique word in s maps to exactly one letter in pattern.
No two letters map to the same word, and no two words map to the same letter. 

Example 1:
    Input: pattern = "abba", s = "dog cat cat dog"
    Output: true
    Explanation:
    The bijection can be established as:
    'a' maps to "dog".
    'b' maps to "cat".

Example 2:
    Input: pattern = "abba", s = "dog cat cat fish"
    Output: false

Example 3:
    Input: pattern = "aaaa", s = "dog cat cat dog"
    Output: false
"""

def word_pattern(pattern, s):
    words = s.split(" ")
    seen = {}

    if len(pattern) != len(words): return False
    if len(set(pattern)) != len(set(words)): return False

    for i in range(len(words)):
        if words[i] not in seen:
            seen[words[i]] = pattern[i]
        elif seen[words[i]] != pattern[i]:
            return False
    return True

p1 = "abba"
s1 = "dog cat cat dog"
p2 = "abba"
s2 = "dog cat cat fish"
print(word_pattern(p1,s1))
print(word_pattern(p2,s2))
