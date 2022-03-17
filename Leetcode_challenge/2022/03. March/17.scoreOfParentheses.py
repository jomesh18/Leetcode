'''
856. Score of Parentheses
Medium

3567

109

Add to List

Share
Given a balanced parentheses string s, return the score of the string.

The score of a balanced parentheses string is based on the following rule:

"()" has score 1.
AB has score A + B, where A and B are balanced parentheses strings.
(A) has score 2 * A, where A is a balanced parentheses string.
 

Example 1:

Input: s = "()"
Output: 1
Example 2:

Input: s = "(())"
Output: 2
Example 3:

Input: s = "()()"
Output: 2
 

Constraints:

2 <= s.length <= 50
s consists of only '(' and ')'.
s is a balanced parentheses string.
Accepted
108,220
Submissions
165,690
'''
O(n), O(n)
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        for c in s:
            if c == ")":
                if stack[-1] == '(':
                    stack[-1] = 1
                else:
                    count = 0
                    while stack[-1] != '(':
                        count += stack.pop()
                    stack[-1] = 2*count
            else:
                stack.append(c)
        return sum(stack)
#O(n), O(1)
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        ans, bal = 0, 0
        for i, c in enumerate(s):
            if c == "(":
                bal += 1
            else:
                bal -= 1
                if s[i-1] == "(":
                    ans += (1<<bal)
        return ans