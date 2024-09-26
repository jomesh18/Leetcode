'''
241. Different Ways to Add Parentheses
Medium

5735

326

Add to List

Share
Given a string expression of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. You may return the answer in any order.

The test cases are generated such that the output values fit in a 32-bit integer and the number of different results does not exceed 104.

 

Example 1:

Input: expression = "2-1-1"
Output: [0,2]
Explanation:
((2-1)-1) = 0 
(2-(1-1)) = 2
Example 2:

Input: expression = "2*3-4*5"
Output: [-34,-14,-10,-10,10]
Explanation:
(2*(3-(4*5))) = -34 
((2*3)-(4*5)) = -14 
((2*(3-4))*5) = -10 
(2*((3-4)*5)) = -10 
(((2*3)-4)*5) = 10
 

Constraints:

1 <= expression.length <= 20
expression consists of digits and the operator '+', '-', and '*'.
All the integer values in the input expression are in the range [0, 99].
The integer values in the input expression do not have a leading '-' or '+' denoting the sign.
'''
class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        memo = {}
        return self._compute(expression, memo, 0, len(expression) - 1)
    
    def _compute(self, s, memo, l, r):
        if l > r:
            return []
        if (l, r) in memo: return memo[(l, r)]
        if r-l <= 1:
            return [int(s[l:r+1])]
        res = []
        for i in range(l, r+1):
            if s[i].isdigit():
                continue
            left = self._compute(s, memo, l, i-1)
            right = self._compute(s, memo, i+1, r)
            
            for l_val in left:
                for r_val in right:
                    if s[i] == '+':
                        res.append(l_val+r_val)
                    elif s[i] == '-':
                        res.append(l_val-r_val)
                    elif s[i] == '*':
                        res.append(l_val*r_val)
        memo[(l, r)] = res
        return res