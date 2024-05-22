'''
131. Palindrome Partitioning
Medium

12545

466

Add to List

Share
Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

 

Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
Example 2:

Input: s = "a"
Output: [["a"]]
 

Constraints:

1 <= s.length <= 16
s contains only lowercase English letters.
'''
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        n = len(s)
        dp = [[False]*n for _ in range(n)]
        def dfs(i, curr):
            if i == n:
                ans.append(curr)
                return
            for end in range(i, n):
                if s[i] == s[end] and (end-i < 3 or dp[i+1][end-1]):
                    dp[i][end] = True
                    dfs(end+1, curr+[s[i:end+1]])
        dfs(0, [])
        return ans