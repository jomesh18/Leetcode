'''
20. Valid Parentheses
Easy

11778

516

Add to List

Share
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
Accepted
2,042,931
Submissions
5,020,569
'''
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == ")":
                if not stack or stack[-1] != "(": return False
                stack.pop()
            elif c == "}":
                if not stack or stack[-1] != "{": return False
                stack.pop()
            elif c == "]":
                if not stack or stack[-1] != "[": return False
                stack.pop()
            else:
                stack.append(c)
        if stack: return False
        return True
