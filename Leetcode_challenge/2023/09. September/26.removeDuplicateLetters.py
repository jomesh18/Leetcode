'''
316. Remove Duplicate Letters
Medium

7585

492

Add to List

Share
Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

 

Example 1:

Input: s = "bcabc"
Output: "abc"
Example 2:

Input: s = "cbacdcbc"
Output: "acdb"
 

Constraints:

1 <= s.length <= 104
s consists of lowercase English letters.
 

Note: This question is the same as 1081: https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/
'''
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        count = Counter(s)
        visited = set()
        stack = []
        for c in s:
            count[c] -= 1
            if c not in visited:
                while stack and stack[-1] > c and count[stack[-1]]:
                    visited.remove(stack[-1])
                    stack.pop()
                stack.append(c)
                visited.add(c)
        return ''.join(stack)
