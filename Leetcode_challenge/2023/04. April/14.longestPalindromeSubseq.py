'''
516. Longest Palindromic Subsequence
Medium

7522

280

Add to List

Share
Given a string s, find the longest palindromic subsequence's length in s.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

 

Example 1:

Input: s = "bbbab"
Output: 4
Explanation: One possible longest palindromic subsequence is "bbbb".
Example 2:

Input: s = "cbbd"
Output: 2
Explanation: One possible longest palindromic subsequence is "bb".
 

Constraints:

1 <= s.length <= 1000
s consists only of lowercase English letters.
'''
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        memo = [[-1]*n for _ in range(n)]
        def helper(l, r):
            if l > r:
                return 0
            elif l == r:
                memo[l][r] = 1
            else:
                if memo[l][r] == -1:
                    if s[l] == s[r]:
                        memo[l][r] = 2 + helper(l+1, r-1)
                    else:
                        memo[l][r] = max(helper(l+1, r), helper(l, r-1))
            return memo[l][r]
        
        return helper(0, n-1)