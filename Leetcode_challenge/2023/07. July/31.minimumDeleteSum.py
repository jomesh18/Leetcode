'''
712. Minimum ASCII Delete Sum for Two Strings
Medium

3196

84

Add to List

Share
Given two strings s1 and s2, return the lowest ASCII sum of deleted characters to make two strings equal.

 

Example 1:

Input: s1 = "sea", s2 = "eat"
Output: 231
Explanation: Deleting "s" from "sea" adds the ASCII value of "s" (115) to the sum.
Deleting "t" from "eat" adds 116 to the sum.
At the end, both strings are equal, and 115 + 116 = 231 is the minimum sum possible to achieve this.
Example 2:

Input: s1 = "delete", s2 = "leet"
Output: 403
Explanation: Deleting "dee" from "delete" to turn the string into "let",
adds 100[d] + 101[e] + 101[e] to the sum.
Deleting "e" from "leet" adds 101[e] to the sum.
At the end, both strings are equal to "let", and the answer is 100+101+101+101 = 403.
If instead we turned both strings into "lee" or "eet", we would get answers of 433 or 417, which are higher.
 

Constraints:

1 <= s1.length, s2.length <= 1000
s1 and s2 consist of lowercase English letters.
'''
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        n1, n2 = len(s1), len(s2)
        pre1, pre2 = [0]*n1, [0]*n2
        prev1, prev2 = 0, 0
        for i in range(n1-1, -1, -1):
            prev1 += ord(s1[i])
            pre1[i] = prev1
        for i in range(n2-1, -1, -1):
            prev2 += ord(s2[i])
            pre2[i] = prev2
        memo = [[None]*n2 for _ in range(n1)]
        def helper(i, j):
            if i == n1 and j == n2: return 0
            if i == n1:
                return pre2[j]
            elif j == n2:
                return pre1[i]
            if memo[i][j] is not None: return memo[i][j];
            if s1[i] == s2[j]:
                memo[i][j] = helper(i+1, j+1)
            else:
                memo[i][j] = min(ord(s1[i]) + helper(i+1, j), ord(s2[j]) + helper(i, j+1))
            return memo[i][j]
        return helper(0, 0)