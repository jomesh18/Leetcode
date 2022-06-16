'''
5. Longest Palindromic Substring
Medium

18504

1088

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
Accepted
1,892,377
Submissions
5,921,059
'''
O(n*n)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        ans = 1
        ind = 0
        for i in range(n):
            right = i
            while right < n and s[i] == s[right]:
                right += 1
            left = i-1
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            if ans < right-left-1:
                ans = right-left-1
                ind = left + 1
        return s[ind: ind+ans]

#dp O(n*n)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        ans = 1
        ans_ind = 0
        dp = [[False]*n for _ in range(n)]
        for i in range(n):
            for j in range(i, -1, -1):
                if s[i] == s[j]:
                    if i - j <= 2 or dp[j+1][i-1]:
                        dp[j][i] = True
                        if ans < i-j+1:
                            ans = i-j+1
                            ans_ind = j
        return s[ans_ind: ans_ind+ans]
    