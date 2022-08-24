'''
Generate Parentheses

Solution
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
 

Constraints:

1 <= n <= 8
'''
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.res = []
        def helper(start, end, curr):
            if start == 0 and end == 0:
                self.res.append(''.join(curr))
                return
            if start:
                helper(start-1, end, curr+['('])
            if end > start:
                helper(start, end-1, curr+[')'])
            
        helper(n, n, [])
        return self.res