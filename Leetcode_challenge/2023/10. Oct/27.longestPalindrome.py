'''
5. Longest Palindromic Substring
Medium

27632

1637

Add to List

Share
Given a string s, return the longest palindromic substring in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False]*n for _ in range(n+1)]
        
        left, length = 0, 1
        for l in range(2):
            dp[l] = [True]*n
            
        for l in range(2, n+1):
            for i in range(n-l+1):
                if s[i] == s[i+l-1] and dp[l-2][i+1]:
                    dp[l][i] = True
                    left = i
                    length = l
        # print(dp)
        return s[left: left+length]