'''
Basic Calculator II

Solution
Given a string s which represents an expression, evaluate this expression and return its value. 

The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

 

Example 1:

Input: s = "3+2*2"
Output: 7
Example 2:

Input: s = " 3/2 "
Output: 1
Example 3:

Input: s = " 3+5 / 2 "
Output: 5
 

Constraints:

1 <= s.length <= 3 * 105
s consists of integers and operators ('+', '-', '*', '/') separated by some number of spaces.
s represents a valid expression.
All the integers in the expression are non-negative integers in the range [0, 231 - 1].
The answer is guaranteed to fit in a 32-bit integer.
'''
class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        i = 0
        while s[i] == ' ': i += 1
        start = i
        while i < len(s) and s[i].isnumeric():
            i += 1
        stack.append(int(s[start:i]))
        while i < len(s):
            while i < len(s) and s[i] == ' ': i += 1
            if i == len(s): break
            op = i
            i += 1
            while s[i] == ' ': i += 1
            start = i
            while i < len(s) and s[i].isnumeric():
                i += 1
            op2 = int(s[start: i])
            if s[op] == '*': stack.append(stack.pop()*op2)
            elif s[op] == '/': stack.append(int(stack.pop()/op2))
            else:
                stack.append('+')
                if s[op] == '-': 
                    op2 *= -1
                stack.append(op2)
        while len(stack) != 1:
            op2 = stack.pop()
            op = stack.pop()
            op1 = stack.pop()
            if op == '+':
                stack.append(op1+op2)
            else:
                stack.append(op1-op2)
        return stack.pop()


#consise
class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        n = len(s)
        operator = '+'
        num = 0
        for i in range(n):
            if s[i].isnumeric():
                num = num * 10 + int(s[i])
            if (not s[i].isnumeric() and s[i] != ' ') or i == n-1:
                if operator == '+':
                    stack.append(num)
                elif operator == '-':
                    stack.append(-num)
                elif operator == '/':
                    stack.append(int(stack.pop()/num))
                elif operator == '*':
                    stack.append(stack.pop()*num)
                num = 0
                operator = s[i]
        return sum(stack)

#O(1) space
class Solution:
    def calculate(self, s: str) -> int:
        n = len(s)
        last_number = 0
        curr_number = 0
        res = 0
        operator = '+'
        for i in range(n):
            if s[i].isnumeric():
                curr_number = curr_number * 10 + int(s[i])
            if (not s[i].isnumeric() and s[i] != ' ') or i == n-1:
                if operator == '+' or operator == '-':
                    res += last_number
                    last_number = curr_number if operator == '+' else -curr_number
                elif operator == '*':
                    last_number *= curr_number
                elif operator == '/':
                    last_number = int(last_number / curr_number)
                curr_number = 0
                operator = s[i]
        return res + last_number