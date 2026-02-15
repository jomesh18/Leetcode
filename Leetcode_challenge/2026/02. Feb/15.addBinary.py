'''
67. Add Binary
Solved
Easy
Topics
premium lock icon
Companies
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
        if len(a) < len(b):
            return self.addBinary(b, a)
        ans = []
        c = 0
        a = a[::-1]
        b = b[::-1]
        for i in range(len(b)):
            curr = int(a[i]) + int(b[i]) + c
            ans.append(str(1 if (curr & 1) else 0))
            c = curr >> 1

        for i in range(len(b), len(a)):
            curr = int(a[i]) + c
            ans.append(str(1 if (curr & 1) else 0))
            c = curr >> 1
        
        if c:
            ans.append(str(c))
        
        return ''.join(ans[::-1])
