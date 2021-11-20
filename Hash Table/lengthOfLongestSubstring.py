'''
Longest Substring Without Repeating Characters

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

Example 4:

Input: s = ""
Output: 0

 

Constraints:

    0 <= s.length <= 5 * 104
    s consists of English letters, digits, symbols and spaces.

'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, j = 0, 0
        found = {}
        res = 0
        for j in range(len(s)):
            c = s[j]
            if c in found:
                res = max(res, j-i)
                i = max(i, found[c] + 1)
            found[c] = j
        return max(res, j-i)

s = "abcabcbb"
# Output: 3

# s = "bbbbb"
# # Output: 1

# s = "pwwkew"
# # Output: 3

# s = ""
# # Output: 0

# s = " "
# Output: 1

s = "abba"
# 2

sol = Solution()
print(sol.lengthOfLongestSubstring(s))
