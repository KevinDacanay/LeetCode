"""
Given an array of strings strs, group the anagrams together. 
You can return the answer in any order.

Example 1:
    Input: strs = ["eat","tea","tan","ate","nat","bat"]
    Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
    Explanation:
    There is no string in strs that can be rearranged to form "bat".
    The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
    The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
Example 2:
    Input: strs = [""]
    Output: [[""]]
Example 3:
    Input: strs = ["a"]
    Output: [["a"]]
"""
def group_anagrams(strs):
    anagrams = {}

    for i in range(len(strs)):
        word = "".join(sorted(strs[i]))
        if word not in anagrams:
            # Create a key value pair: sorted word -> list of word
            anagrams[word] = [strs[i]]
        else:
            # If word already in anagrams, append the string to the list value
            anagrams[word].append(strs[i])
    return anagrams.values()

s1 = ["eat","tea","tan","ate","nat","bat"]
s2 = [""]
s3 = ["a"]
print(group_anagrams(s1))
print(group_anagrams(s))
print(group_anagrams(s3))