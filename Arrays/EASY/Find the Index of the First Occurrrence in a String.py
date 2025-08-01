"""
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
 

Constraints:

1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters.
"""
def strStr(haystack, needle):
        need = len(needle)
        hay = len(haystack)
        index = 0       # index to be returned

        # edge cases:
        if need > hay or hay == 0 or need == 0:
            return -1

        # iterate for the length of length of haystack - needle + 1
        for i in range(hay - need + 1):
            # counter for number of the same chars for substring
            j = 0   # counter for haystack
            k = 0   # counter for needle

            if haystack[i] == needle[j]:
                # found a matching first letter 
                index = i
            # check the subsequent chars ([j + i] since we check at index i for the 
            # entire iteration of the current while loop. i just determines which char
            # we start at. j determines the subsequest chars) 
            while j < need and haystack[j + i] == needle[k]:
                j += 1
                k += 1

            # if found a whole match, return the index:
            if j == need:
                return index
        return -1

h1 = "sadbutsad"
n1 = "sad"
print(strStr(h1, n1))

h2 = "leetcode"
n2 = "leeto"
print(strStr(h2, n2))

h3 = "mississippi"
n3 = "issipi"
print(strStr(h3, n3))