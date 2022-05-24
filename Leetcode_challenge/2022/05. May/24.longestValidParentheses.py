'''
32. Longest Valid Parentheses
Hard

8024

270

Add to List

Share
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

 

Example 1:

Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".
Example 2:

Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".
Example 3:

Input: s = ""
Output: 0
 

Constraints:

0 <= s.length <= 3 * 104
s[i] is '(', or ')'.
'''
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        res = 0
        stack = [-1]
        for i, ch in enumerate(s):
            if ch == "(":
                stack.append(i)
            else:
                stack.pop()
                if stack:
                    res = max(i-stack[-1], res)
                else:
                    stack.append(i)
        return res

        