'''
Interleaving String

Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

An interleaving of two strings s and t is a configuration where they are divided into non-empty substrings such that:

    s = s1 + s2 + ... + sn
    t = t1 + t2 + ... + tm
    |n - m| <= 1
    The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...

Note: a + b is the concatenation of strings a and b.

 

Example 1:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true

Example 2:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false

Example 3:

Input: s1 = "", s2 = "", s3 = ""
Output: true

 

Constraints:

    0 <= s1.length, s2.length <= 100
    0 <= s3.length <= 200
    s1, s2, and s3 consist of lowercase English letters.

 

Follow up: Could you solve it using only O(s2.length) additional memory space?
'''

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # print(s1, s2, s3)   
        while s1 and s2:
            part = ""
            for s in s1:
                if s3.startswith(s):
                    part += s
                    s3 = s3.replace(s, "", 1)
                else:
                    break
            if len(part) == 0:
                return False
            else:
                s1 = s1.replace(part, "", 1)
            part = ""
            for s in s2:
                if s3.startswith(s):
                    part += s
                    s3 = s3.replace(s, "", 1)
                else:
                    break
            if len(part) == 0:
                return False
            else:
                s2 = s2.replace(part, "", 1)
            # print(s1, s2, s3)
        if not s1 and not s2:
            return not s3
        if s1:
            if s1 == s3:
                return True
        elif s2:
            if s2 == s3:
                return True

s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"
# Output: true
s1 = ""
s2 = ""
s3 = ""
# Output: true
s1 = "a"
s2 = "b"
s3 = "ab"
# Output: true

s = Solution()
print(s.isInterleave(s1, s2, s3))
