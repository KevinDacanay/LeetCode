"""
You're given strings jewels representing the types of stones that are jewels, 
and stones representing the stones you have. Each character in stones is a 
type of stone you have. You want to know how many of the stones you have are also jewels.
Letters are case sensitive, so "a" is considered a different type of stone from "A".

Example 1:
    Input: jewels = "aA", stones = "aAAbbbb"
    Output: 3

Example 2:
    Input: jewels = "z", stones = "ZZ"
    Output: 0
"""
def num_jewels_in_stones(jewels, stones):
    j = set(jewels)
    count = 0
    for char in range(len(stones)):
        if stones[char] in j:
            count += 1
    return count

print(num_jewels_in_stones(jewels="aA", stones="aAAbbbb"))
print(num_jewels_in_stones(jewels="z", stones="ZZ"))