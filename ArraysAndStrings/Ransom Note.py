"""
Given two strings ransomNote and magazine, return true if 
ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

Example 1:
    Input: ransomNote = "a", magazine = "b"
    Output: false
Example 2:
    Input: ransomNote = "aa", magazine = "ab"
    Output: false
Example 3:
    Input: ransomNote = "aa", magazine = "aab"
    Output: true
"""
def can_construct(ransom_note, magazine):
    r = list(ransom_note)
    m = list(magazine)
    for i in range(len(ransom_note)):
        if ransom_note[i] not in m:
            return False
        else:
            m.remove(ransom_note[i])
    return True