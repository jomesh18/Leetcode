'''
647. Palindromic Substrings
Medium

10141

218

Add to List

Share
Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.

 

Example 1:

Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
Example 2:

Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
 

Constraints:

1 <= s.length <= 1000
s consists of lowercase English letters.
'''
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[0]*n for _ in range(n+1)]
        for i in range(n):
            dp[1][i] = 1
        ans = n
        for l in range(2, n+1):
            for j in range(n-l+1):
                if s[j] == s[j+l-1] and (l <= 2 or dp[l-2][j+1]):
                    ans += 1
                    dp[l][j] = 1
        # print(dp)
        return ans