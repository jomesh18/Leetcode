'''
583. Delete Operation for Two Strings
Medium

3473

54

Add to List

Share
Given two strings word1 and word2, return the minimum number of steps required to make word1 and word2 the same.

In one step, you can delete exactly one character in either string.

 

Example 1:

Input: word1 = "sea", word2 = "eat"
Output: 2
Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".
Example 2:

Input: word1 = "leetcode", word2 = "etco"
Output: 4
 

Constraints:

1 <= word1.length, word2.length <= 500
word1 and word2 consist of only lowercase English letters.
'''
#dp, O(m*n)
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0]*n for _ in range(m)]
        dp[0][0] = 1 if word1[0] == word2[0] else 0
        for i in range(1, n):
            dp[0][i] = dp[0][i-1] | (1 if word1[0] == word2[i] else 0)
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] | (1 if word1[i] == word2[0] else 0)
            
        for i in range(1, m):
            for j in range(1, n):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return m+n-2*dp[-1][-1]

# recursion with memoization
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        memo = {}
        def lcs(i, j):
            print(i, j)
            if (i, j) in memo: return memo[(i, j)]
            if i == m or j == n: return 0
            ans = 0
            if word1[i] == word2[j]:
                ans = 1 + lcs(i+1, j+1)
            else:
                ans = max(lcs(i, j+1), lcs(i+1, j))
            memo[(i, j)] = ans
            return ans
        return m+n-2*lcs(0, 0)