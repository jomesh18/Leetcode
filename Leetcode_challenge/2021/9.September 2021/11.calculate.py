'''
Basic Calculator
Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

 

Example 1:

Input: s = "1 + 1"
Output: 2
Example 2:

Input: s = " 2-1 + 2 "
Output: 3
Example 3:

Input: s = "(1+(4+5+2)-3)+(6+8)"
Output: 23
 

Constraints:

1 <= s.length <= 3 * 105
s consists of digits, '+', '-', '(', ')', and ' '.
s represents a valid expression.
'+' is not used as a unary operation.
'-' could be used as a unary operation but it has to be inside parentheses.
There will be no two consecutive operators in the input.
Every number and running calculation will fit in a signed 32-bit integer.
'''
# my try, not correct
# class Solution:
#     def calculate(self, s: str) -> int:
        # stack = []
        # i = 0
        # while i < len(s):
        #     c = s[i]
        #     if c.isdigit():
        #         if stack and (stack[-1] == "+" or stack[-1] == "-"):
        #             operator = stack.pop()
        #             operand1 = stack.pop()
        #             if operator == "+":
        #                 stack.append(str(int(operand1)+int(c)))
        #             if operator == "-":
        #                 stack.append(str(int(operand1)-int(c)))
        #         else:
        #             stack.append(c)
        #     elif c == ")":
        #         if stack[-1] == "-":
        #             stack.pop()
        #             stack.pop()
        #             i += 1
        #             stack.append("-"+s[i])
        #         elif stack[-2] == "(":
        #             operand2 = stack.pop()
        #             stack.pop()
        #             stack.append(str(operand2))
        #         else:
        #             operand2 = stack.pop()
        #             operator = stack.pop()
        #             operand1 = stack.pop()
        #             if operator == "+":
        #                 operand2 = int(operand2)+int(operand1)
        #             if operator == "-":
        #                 operand2 = int(operand2)-int(operand1)
        #             if stack[-1] == "(":
        #                 stack.pop()
        #             stack.append(str(operand2))
        #     elif c == " ":
        #         i += 1
        #         continue
        #     else:
        #         stack.append(c)
        #     print(stack)
        #     i += 1

        # while len(stack)>1:
        #     operand2 = stack.pop()
        #     operator = stack.pop()
        #     operand1 = stack.pop()
        #     if operator == "+":
        #         operand2 = int(operand2)+int(operand1)
        #     if operator == "-":
        #         operand2 = int(operand2)-int(operand1)
        #     stack.append(operand2)
        # return int(stack[-1])

#from leetcode
# class Solution:
#     def calculate(self, s):
#         res, num, sign, stack = 0, 0, 1, []
#         for ss in s:
#             if ss.isdigit():
#                 num = 10*num + int(ss)
#             elif ss in ["-", "+"]:
#                 res += sign*num
#                 num = 0
#                 sign = [-1, 1][ss=="+"]
#             elif ss == "(":
#                 stack.append(res)
#                 stack.append(sign)
#                 sign, res = 1, 0
#             elif ss == ")":
#                 res += sign*num
#                 res *= stack.pop()
#                 res += stack.pop()
#                 num = 0
#         return res + num*sign

s = "1 + 1"
# Output: 2

s = " 2-1 + 2 "
# # Output: 3

s = "(1+(4+5+2)-3)+(6+8)"
# # Output: 23

sol = Solution()
print(sol.calculate(s))
