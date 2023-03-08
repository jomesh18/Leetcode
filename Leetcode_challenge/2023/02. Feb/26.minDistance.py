'''
72. Edit Distance
Hard

12064

140

Add to List

Share
Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character
 

Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
 

Constraints:

0 <= word1.length, word2.length <= 500
word1 and word2 consist of lowercase English letters.
'''
# O(n1*n2), memo
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1, n2 = len(word1), len(word2)
        memo = {}
        def helper(i, j):
            if (i, j) not in memo:
                ans = 0
                if i == n1 or j == n2:
                    ans = max(n1-i, n2-j)
                elif word1[i] != word2[j]:
                    ans = helper(i, j+1)
                    ans = min(ans, helper(i+1, j))
                    ans = min(ans, helper(i+1, j+1))
                    ans += 1
                else: 
                    ans = helper(i+1, j+1)
                memo[(i, j)] = ans
            return memo[(i, j)]
        return helper(0, 0)

# O(n1*n2), tabulation
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:        
        n1, n2 = len(word1), len(word2)
        dp = [[0]*(n2+1) for _ in range(n1+1)]
        for i in range(n1):
            dp[i][n2] = n1-i
        for i in range(n2):
            dp[n1][i] = n2-i
        for i in range(n1-1, -1, -1):
            for j in range(n2-1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    dp[i][j] = 1 + min(dp[i+1][j], dp[i][j+1], dp[i+1][j+1])
        return dp[0][0]