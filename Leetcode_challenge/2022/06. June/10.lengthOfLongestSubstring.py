'''
3. Longest Substring Without Repeating Characters
Medium

24394

1079

Add to List

Share
Given a string s, find the length of the longest substring without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
Accepted
3,371,884
Submissions
10,158,215
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        l = 0
        ans = 0
        d = {}
        curr = 0
        for r in range(n):
            if s[r] in d and d[s[r]] >= l:
                ans = max(r-l, ans)
                l = d[s[r]]+1
            d[s[r]] = r
        return max(ans, n-l)