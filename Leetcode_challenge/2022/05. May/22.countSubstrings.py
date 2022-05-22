'''
647. Palindromic Substrings
Medium

6580

157

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
Accepted
419,454
Submissions
644,777
'''
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False]*n for _ in range(n+2)]
        
        for l in range(1, n+1):
            for start in range(n-l+1):
                dp[l][start] = (s[start] == s[start+l-1]) and (dp[l-2][start+1] if l > 2 else True)
                
        # print(dp)
        return sum(sum(l) for l in dp)