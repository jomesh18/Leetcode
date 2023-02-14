'''
67. Add Binary
Easy

6985

716

Add to List

Share
Given two binary strings a and b, return their sum as a binary string.

 

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
 

Constraints:

1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.
'''
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        c = 0
        if len(b) > len(a):
            a, b = b, a
        res = []
        for i in range(-1, -len(a)-1, -1):
            ta, tb = int(a[i]), int(b[i]) if -i <= len(b) else 0
            t = ta+tb+c
            if t == 0:
                res.append('0')
            elif t == 1:
                res.append('1')
                c = 0
            elif t == 2:
                res.append('0')
                c = 1
            else:
                res.append('1')
                c = 1
        if c:
            res.append('1')
        return ''.join(res[::-1])