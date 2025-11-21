'''
1930. Unique Length-3 Palindromic Subsequences
Solved
Medium
Topics
premium lock icon
Companies
Hint
Given a string s, return the number of unique palindromes of length three that are a subsequence of s.

Note that even if there are multiple ways to obtain the same subsequence, it is still only counted once.

A palindrome is a string that reads the same forwards and backwards.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
 

Example 1:

Input: s = "aabca"
Output: 3
Explanation: The 3 palindromic subsequences of length 3 are:
- "aba" (subsequence of "aabca")
- "aaa" (subsequence of "aabca")
- "aca" (subsequence of "aabca")
Example 2:

Input: s = "adc"
Output: 0
Explanation: There are no palindromic subsequences of length 3 in "adc".
Example 3:

Input: s = "bbcbaba"
Output: 4
Explanation: The 4 palindromic subsequences of length 3 are:
- "bbb" (subsequence of "bbcbaba")
- "bcb" (subsequence of "bbcbaba")
- "bab" (subsequence of "bbcbaba")
- "aba" (subsequence of "bbcbaba")
 

Constraints:

3 <= s.length <= 105
s consists of only lowercase English letters.
'''
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        pos = {i: [] for i in range(26)}
        for i in range(len(s)):
            pos[ord(s[i]) - ord('a')].append(i)
        ans = 0
        for i in range(26):
            if len(pos[i]) < 2:
                continue
            f, l = pos[i][0], pos[i][-1]
            # print(i)
            for j in range(26):
                if i != j:
                    k = bisect_left(pos[j], f)
                    if k == len(pos[j]) or pos[j][k] < f or pos[j][k] > l:
                        continue
                    ans += 1
                    # print(j, pos[j], f, k, ans)
                elif len(pos[i]) > 2:
                    ans += 1
                    # print(j, pos[j], f, ans)
            
        return ans
