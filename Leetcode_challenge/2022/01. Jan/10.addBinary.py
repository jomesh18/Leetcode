'''
67. Add Binary
Easy

4104

473

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
Accepted
742,490
Submissions
1,499,995
'''
#iterative version (intuitive)
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        diff = len(a) - len(b)
        if diff > 0:
            b = "0"*diff + b
        if diff < 0:
            a = "0"*-diff + a
        carry = 0
        l = len(a) - 1
        res = ''
        
        while l >= 0:
            s = int(a[l]) + int(b[l]) + carry
            if s == 2:
                carry = 1
                res = '0' + res
            elif s == 3:
                carry = 1
                res = '1' + res
            else:
                res = str(s) + res
                carry = 0
            l -= 1
        if carry:
            res = str(carry) + res
        return res


#using recursive approach
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if not a or not b: return a or b

        if a[-1] == '1' and b[-1] == '1':
            return self.addBinary(self.addBinary(a[:-1], b[:-1]), '1') + '0'
        elif a[-1] == '0' and b[-1] == '0':
            return self.addBinary(a[:-1], b[:-1]) + '0'
        else:
            return self.addBinary(a[:-1], b[:-1]) + '1'

#iterative version
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a, b = list(a), list(b)
        c = 0
        res = ""
        while a or b or c:
            if a:
                c += int(a.pop())
            if b:
                c += int(b.pop())
            res += str(c % 2)
            c //= 2
        return res[::-1]

a = "11"
b = "1"
# Output: "100"

a = "1010"
b = "1011"
# Output: "10101"

sol = Solution()
print(sol.addBinary(a, b))

