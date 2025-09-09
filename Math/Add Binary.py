"""
Given two binary strings a and b, return their sum as a binary string.

Example 1:
    Input: a = "11", b = "1"
    Output: "100"

Example 2:
    Input: a = "1010", b = "1011"
    Output: "10101"
"""

def addBinary1(a, b):    
    return bin(int(a,2) + int(b,2))[2:]

def addBinary2(a, b):
    dec_a = int(a, 2)
    dec_b = int(b, 2)
    return bin(dec_a + dec_b)[2:]