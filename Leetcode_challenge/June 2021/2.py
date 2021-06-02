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
#from leetcode

# class Solution:
#     def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
#         def helper(s1, i, s2, j, res, s3):
#             # if not s3.startswith(res):
#             #     return False
#             if res == s3 and i == len(s1) and j == len(s2):
#                 return True
#             ans = False
#             if i < len(s1):
#                 # ans = ans or helper(s1, i+1, s2, j, res+s1[i], s3)
#                 ans |= helper(s1, i+1, s2, j, res+s1[i], s3)
#             if j < len(s2):
#                 # ans = ans or helper(s1, i, s2, j+1, res+s2[j], s3)
#                 ans |= helper(s1, i, s2, j+1, res+s2[j], s3)
#             return ans
#         if len(s1) + len(s2) != len(s3):
#             return False
#         else:
#             return helper(s1, 0, s2, 0, "", s3)


#from leetcode, recursive, with memoization

# class Solution:
#     def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

#         def helper(s1, i, s2, j, s3, k, memo):
#             if i == len(s1):
#                 return s2[j:] == s3[k:]
#             elif j == len(s2):
#                 return s1[i:] == s3[k:]
#             if memo[i][j] >= 0:
#                 return memo[i][j]
#             else:
#                 ans = False
#                 if s3[k] == s1[i] and helper(s1, i+1, s2, j, s3, k+1, memo) or s3[k] == s2[j] and helper(s1, i, s2, j+1, s3, k+1, memo):
#                     ans = True
#                 memo[i][j] = ans
#                 return ans
 
#         memo = [[-1 for i in range(len(s2))] for j in range(len(s1))]
#         if len(s1) + len(s2) != len(s3):
#             return False
#         else:
#             return helper(s1, 0, s2, 0, s3, 0, memo)

#using dp
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        dp = [[None for j in range(len(s2)+1)] for i in range(len(s1)+1)]

        for i in range(len(s1)+1):
            for j in range(len(s2)+1):
                if i == 0 and j == 0:
                    dp[i][j] = True
                elif i == 0:
                    dp[i][j] = dp[i][j-1] and s2[j-1] == s3[i+j-1]
                elif j == 0:
                    dp[i][j] = dp[i-1][j] and s1[i-1] == s3[i+j-1]
                else:
                    dp[i][j] = dp[i-1][j] and s1[i-1] == s3[i+j-1] or dp[i][j-1] and s2[j-1] == s3[i+j-1]
        print(dp)
        return dp[len(s1)][len(s2)]

# s1 = "aabcc"
# s2 = "dbbca"
# s3 = "aadbbcbcac"
# Output: true
# s1 = ""
# s2 = ""
# s3 = ""
# # Output: true
# s1 = "a"
# s2 = "b"
# s3 = "ab"
# # Output: true
s1 = "aa"
s2 = "ab"
s3 = "aaba"

s = Solution()
print(s.isInterleave(s1, s2, s3))
