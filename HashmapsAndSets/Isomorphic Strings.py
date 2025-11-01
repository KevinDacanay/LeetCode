"""
Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s 
can be replaced to get t. All occurrences of a character must 
be replaced with another character while preserving the order 
of characters. No two characters may map to the same character, 
but a character may map to itself.

Example 1:
    Input: s = "egg", t = "add"
    Output: true
    Explanation: The strings s and t can be made identical by:
        Mapping 'e' to 'a'.
        Mapping 'g' to 'd'.
Example 2:
    Input: s = "foo", t = "bar"
    Output: false
    Explanation: The strings s and t can not be made identical 
        as 'o' needs to be mapped to both 'a' and 'r'.
Example 3:
    Input: s = "paper", t = "title"
    Output: true
"""
def is_isomorphic(s,t):
    if len(s) != len(t): return False

    s_m = {}
    t_m = {}
    for i in range(len(s)):
        if s[i] not in s_m:
            s_m[s[i]] = i
        if t[i] not in t_m:
            t_m[t[i]] = i
        if s_m[s[i]] != t_m[t[i]]:
            return False
    return True

if __name__=="__main__":
    s1 = "egg"; t1 = "add"
    s2 = "foo"; t2 = "bar"
    s3 = "paper"; t3 = "title"
    print(is_isomorphic(s1,t1))
    print(is_isomorphic(s2,t2))
    print(is_isomorphic(s3,t3))