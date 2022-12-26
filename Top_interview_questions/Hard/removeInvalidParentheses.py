'''
Remove Invalid Parentheses

Solution
Given a string s that contains parentheses and letters, remove the minimum number of invalid parentheses to make the input string valid.

Return all the possible results. You may return the answer in any order.

 

Example 1:

Input: s = "()())()"
Output: ["(())()","()()()"]
Example 2:

Input: s = "(a)())()"
Output: ["(a())()","(a)()()"]
Example 3:

Input: s = ")("
Output: [""]
 

Constraints:

1 <= s.length <= 25
s consists of lowercase English letters and parentheses '(' and ')'.
There will be at most 20 parentheses in s.
'''
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        n = len(s)
        ans = {""}
        def backtrack(i, curr, t):
            nonlocal ans
            if i == n:
                if t == 0:
                    temp = ans.pop()
                    if len(temp) == len(curr):
                        ans.add(curr)
                        ans.add(temp)
                    elif len(curr) > len(temp):
                        ans = {curr}
                    elif len(temp) > len(curr):
                        ans.add(temp)
                return
            if s[i] == "(":
                backtrack(i+1, curr+s[i], t+1)
                backtrack(i+1, curr, t)
            elif s[i] == ')':
                if t > 0:
                    backtrack(i+1, curr+s[i], t-1)
                backtrack(i+1, curr, t)
            else:
                backtrack(i+1, curr+s[i], t)
        backtrack(0, '', 0)
        return list(ans)
    
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        n, left, right = len(s), 0, 0
        for c in s:
            if c == '(':
                left += 1
            elif c == ')':
                if left:
                    left -= 1
                else:
                    right += 1
        to_remove = left + right
        ans = set()
        def backtrack(i, curr, tot, left_removed, right_removed):
            if i == n:
                if tot == 0:
                    ans.add(curr)
            else:
                if s[i] == '(' and left_removed < left:
                    backtrack(i+1, curr, tot, left_removed+1, right_removed)
                elif s[i] == ')' and right_removed < right:
                    backtrack(i+1, curr, tot, left_removed, right_removed+1)
                if s[i] != '(' and s[i] != ')':
                    backtrack(i+1, curr+s[i], tot, left_removed, right_removed)
                elif s[i] == '(':
                    backtrack(i+1, curr+s[i], tot+1, left_removed, right_removed)
                elif s[i] == ')' and tot > 0:
                    backtrack(i+1, curr+s[i], tot-1, left_removed, right_removed)
            
        backtrack(0, '', 0, 0, 0)
        return list(ans)


# bfs
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        ans = []
        q = [s]
        seen = {s}
        def is_valid(node):
            c = 0
            for ch in node:
                if ch == '(':
                    c += 1
                elif ch == ')':
                    if c == 0:
                        return False
                    c -= 1
            return c == 0
        while q:
            newq = []
            for node in q:
                if is_valid(node):
                    ans.append(node)
                if not ans:
                    for i in range(len(node)):
                        if node[i] == '(' or node[i] == ')':
                            new_node = node[:i]+node[i+1:]
                            if new_node not in seen:
                                newq.append(new_node)
                                seen.add(new_node)
            q = newq
            
        return ans