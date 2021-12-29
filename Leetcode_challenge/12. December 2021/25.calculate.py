'''
227. Basic Calculator II
Medium

3693

493

Add to List

Share
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
#using stack, O(n) space, time
# class Solution:
#     def calculate(self, s: str) -> int:
#         stack = []
#         res = 0
#         curr_num = 0
#         operation = '+'
#         for i in range(len(s)):
#             c = s[i]
#             if c.isdigit():
#                 curr_num = curr_num*10 + int(c)
#             if not c.isdigit() and c != ' ' or i == len(s)-1:
#                 if operation == "+":
#                     stack.append(curr_num)
#                 elif operation == "-":
#                     stack.append(-curr_num)
#                 elif operation == "/":
#                     last_num = stack.pop()
#                     stack.append(int(last_num/curr_num))
#                 elif operation == "*":
#                     last_num = stack.pop()
#                     stack.append(last_num*curr_num)
#                 operation = c
#                 curr_num = 0
#         while stack:
#             res += stack.pop()
#         return res

#O(1) space, O(n) time
class Solution:
    def calculate(self, s: str) -> int:
        last_num, curr_num, res, operation = 0, 0, 0, "+"
        for i in range(len(s)):
            c = s[i]
            if c.isdigit():
                curr_num = curr_num*10+int(c)
            if not c.isdigit() and c != " " or i == len(s)-1:
                if operation == "+":
                    res += last_num
                    last_num = curr_num
                elif operation == "-":
                    res += last_num
                    last_num = -curr_num
                elif operation == "/":
                    last_num = int(last_num/curr_num)
                elif operation == "*":
                    last_num = last_num*curr_num
                operation = c
                curr_num = 0
            # print(i, last_num, curr_num, res, operation)
        return res+last_num

s = "3+2*2"
# Output: 7

s = " 3/2 "
# # # # # # Output: 1
# 
s = " 3+5 / 2 "
# # # # # # Output: 5

s = "0-2147483647"
# # # # # Output: -2147483647

s = "14-3/2"
# # # Output: 13

sol = Solution()
print(sol.calculate(s))
