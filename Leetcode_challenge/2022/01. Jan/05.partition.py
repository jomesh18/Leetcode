'''
131. Palindrome Partitioning
Medium

5336

158

Add to List

Share
Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

A palindrome string is a string that reads the same backward as forward.

 

Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
Example 2:

Input: s = "a"
Output: [["a"]]
 

Constraints:

1 <= s.length <= 16
s contains only lowercase English letters.
Accepted
390,832
Submissions
684,312
'''
# class Solution:
#     def partition(self, s: str) -> [[str]]:
#         def is_palindrome(beg, end):
#             while beg < end:
#                 if s[beg] != s[end]:
#                     return False
#                 beg += 1
#                 end -= 1
#             return True
#         self.res = []
#         def dfs(temp_res, beg, end, inserted):
#             if end == len(s):
#                 if inserted:
#                     self.res.append(temp_res)
#                 return
            
#             if is_palindrome(beg, end):
#                 dfs(temp_res+[s[beg:end+1]], end+1, end+1, True)
#             dfs(temp_res, beg, end+1, False)
                
#         dfs([], 0, 0, False)
#         return self.res


# class Solution:
#     def partition(self, s: str) -> [[str]]:
#         self.res = []
#         def is_palindrome(beg, end):
#             while beg < end:
#                 if s[beg] != s[end]:
#                     return False
#                 beg += 1
#                 end -= 1
#             return True

#         def dfs(start, temp_res):
#             if start == len(s): self.res.append(temp_res[:])
#             for end in range(start, len(s)):
#                 if is_palindrome(start, end):
#                     dfs(end+1, temp_res+[s[start:end+1]])
#         dfs(0, [])
#         return self.res


#using dp to check for palindrome
# class Solution:
#     def partition(self, s: str) -> [[str]]:
#         self.ans = []
#         self.dp = [[False for _ in range(len(s))] for _ in range(len(s))]
#         def dfs(start, temp_res):
#             if start == len(s): self.ans.append(temp_res[:])
#             for end in range(start, len(s)):
#                 if s[start] == s[end] and (end-start<=2 or self.dp[start+1][end-1]):
#                     self.dp[start][end] = True
#                     dfs(end+1, temp_res+[s[start:end+1]])
#         dfs(0, [])
#         return self.ans

#bottom up dp solution
class Solution:
    def partition(self, s: str) -> [[str]]:
        dp = [[] for _ in range(len(s)+1)]
        dp[-1] = [[]]
        for i in range(len(s)-1, -1, -1):
            for j in range(i+1, len(s)+1):
                st = s[i:j]
                if st == st[::-1]:
                    for each in dp[j]:
                        dp[i].append([st]+each)
        return dp[0]

s = "aab"
# Output: [["a","a","b"],["aa","b"]]

# s = "a"
# Output: [["a"]]

# s = "aababaabbaababaa"

sol = Solution()
print(sol.partition(s))
