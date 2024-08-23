'''
592. Fraction Addition and Subtraction
Medium

553

583

Add to List

Share
Given a string expression representing an expression of fraction addition and subtraction, return the calculation result in string format.

The final result should be an irreducible fraction. If your final result is an integer, change it to the format of a fraction that has a denominator 1. So in this case, 2 should be converted to 2/1.

 

Example 1:

Input: expression = "-1/2+1/2"
Output: "0/1"
Example 2:

Input: expression = "-1/2+1/2+1/3"
Output: "1/3"
Example 3:

Input: expression = "1/3-1/2"
Output: "-1/6"
 

Constraints:

The input string only contains '0' to '9', '/', '+' and '-'. So does the output.
Each fraction (input and output) has the format ±numerator/denominator. If the first input fraction or the output is positive, then '+' will be omitted.
The input only contains valid irreducible fractions, where the numerator and denominator of each fraction will always be in the range [1, 10]. If the denominator is 1, it means this fraction is actually an integer in a fraction format defined above.
The number of given fractions will be in the range [1, 10].
The numerator and denominator of the final result are guaranteed to be valid and in the range of 32-bit int.
'''
class Solution:
    def fractionAddition(self, expression: str) -> str:
        stack = []
        curr = 1
        for i, c in enumerate(expression):
            if c == '-':
                curr = -1       
            elif c == '+':
                curr = 1
            elif c == '/':
                curr = 1
            elif c == '0':
                continue
            elif c == '1':
                if i == len(expression)-1 or expression[i+1] != '0':
                    stack.append(curr*int(c))
                else:
                    stack.append(curr*10)
            elif c.isnumeric():
                stack.append(curr * int(c))
            if len(stack) == 4:
                d2, n2, d1, n1 = stack.pop(), stack.pop(), stack.pop(), stack.pop()
                # print(n1, d1, n2, d2)
                stack.append(n1*d2 + n2 * d1)
                stack.append(d1*d2)
            # print(stack, curr)
        denom, numer = stack.pop(), stack.pop()
        if denom == 0 or numer == 0: return '0/1'
        # print(denom, numer)
        sign = -1 if ((numer >= 0) ^ (denom >= 0)) else 1
        numer = abs(numer)
        denom = abs(denom)
        for num in range(min(numer, denom), 1, -1):
            if numer % num == 0 and denom % num == 0:
                numer //= num
                denom //= num
                if numer == 1 or denom == 1:
                    break
        ret = str(numer)+'/'+str(denom)
        # print(sign)
        return '-'+ret if sign == -1 else ret
        