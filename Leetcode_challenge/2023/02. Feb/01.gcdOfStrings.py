'''
1071. Greatest Common Divisor of Strings
Easy

2115

365

Add to List

Share
For two strings s and t, we say "t divides s" if and only if s = t + ... + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

 

Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""
 

Constraints:

1 <= str1.length, str2.length <= 1000
str1 and str2 consist of English uppercase letters.
'''
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1) < len(str2):
            str1, str2 = str2, str1
        ans = ''
        for i in range(len(str2)):
            curr = str2[:i+1]
            divisor = True
            l = len(curr)
            for j in range(0, len(str1)-l+1, l):
                for k in range(l):
                    if str1[j+k] != curr[k] or str2[(j+k)%len(str2)] != curr[k]:
                        divisor = False
                        break
                
            if divisor and not len(str1) % len(curr) and not len(str2)%len(curr):
                ans = curr
        return ans


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1) < len(str2):
            str1, str2 = str2, str1
        for i in range(len(str2)-1, -1, -1):
            curr = str2[:i+1]
            divisor = True
            l = len(curr)
            if len(str1)%l or len(str2)%l:
                continue
            for j in range(0, len(str1)-l+1, l):
                for k in range(l):
                    if str1[j+k] != curr[k] or str2[(j+k)%len(str2)] != curr[k]:
                        divisor = False
                        break
            if divisor:
                return curr
        return ''



class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        l1, l2 = len(str1), len(str2)
        def valid(k):
            if l1 % k or l2 % k:
                return False
            n1, n2 = l1 // k, l2 // k
            curr = str1[:k]
            return curr*n1 == str1 and curr*n2 == str2
        
        for i in range(min(l1, l2), 0, -1):
            if valid(i):
                return str1[:i]
        return ''

# using gcd, math
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1+str2 != str2+str1: return ''
        gcd_len = gcd(len(str1), len(str2))
        return str1[:gcd_len]