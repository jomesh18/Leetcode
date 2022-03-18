'''
316. Remove Duplicate Letters
Medium

4340

293

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

Accepted
164,142
Submissions
389,637
'''
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        visited = [0]*26
        count = [0]*26
        for c in s:
            idx = ord(c)-ord('a')
            count[idx] += 1
        for c in s:
            idx = ord(c)-ord('a')
            count[idx] -= 1
            if not visited[idx]:
                while stack and stack[-1] > idx and count[stack[-1]]:
                    visited[stack[-1]] = 0
                    stack.pop()
                stack.append(idx)
                visited[idx] = 1
        return "".join([chr(ord('a')+idx) for idx in stack])