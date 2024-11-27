'''
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII,
 which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for 
four is not IIII. Instead, the number four is written as IV. Because the one is before the five we 
subtract it making four. The same principle applies to the number nine, which is written as IX. 
There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.


Example 1:

Input: s = "III"
Output: 3
Explanation: III = 3.
Example 2:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 3:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
 

Constraints:

1 <= s.length <= 15
s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
It is guaranteed that s is a valid roman numeral in the range [1, 3999].
'''
    
def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """

    roman = {
        "I": 1,
        "V": 5, 
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    
    result = 0
    i = 0

    while i < len(s):
        if i < len(s) - 1 and s[i] == "I" and s[i+1] == "V":
            i += 2
            result += 4
        elif i < len(s) - 1 and s[i] == "I" and s[i+1] == "X":
            i += 2
            result += 9
        elif i < len(s) - 1 and s[i] == "X" and s[i+1] == "L":
            i += 2
            result += 40
        elif i < len(s) - 1 and s[i] == "X" and s[i+1] == "C":
            i += 2
            result += 90
        elif i < len(s) - 1 and s[i] == "C" and s[i+1] == "D":
            i += 2
            result += 400
        elif i < len(s) - 1 and s[i] == "C" and s[i+1] == "M":
            i += 2
            result += 900 
        else:
            result += roman[s[i]]
            i += 1
    return result
    


test1 = "III"
test2 = "LVIII"
test3 = "MCMXCIV"
test4 = "IV"

test_case = [test1, test2, test3, test4]

for i in test_case:
    print(romanToInt(i))  




# Other Implementation:
print("\n8ms Runtime:")
def romanToInt(s) :
    translations = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    number = 0
    s = s.replace("IV", "IIII").replace("IX", "VIIII")
    s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
    s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
    for char in s:
        number += translations[char]
    return number

test1 = "III"
test2 = "LVIII"
test3 = "MCMXCIV"
test4 = "IV"

test_case = [test1, test2, test3, test4]

for i in test_case:
    print(romanToInt(i)) 


print("\n0ms Runtime")
def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    dictionary = { 'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    total = 0
    prev_value = 0

    for char in reversed(s):
        current_value = dictionary[char]

        if current_value < prev_value:
            total -= current_value
        else:
            total += current_value

        prev_value = current_value
    return total

test1 = "III"
test2 = "LVIII"
test3 = "MCMXCIV"
test4 = "IV"

test_case = [test1, test2, test3, test4]

for i in test_case:
    print(romanToInt(i))  