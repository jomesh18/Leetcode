'''
166. Fraction to Recurring Decimal
Solved
Medium
Topics
premium lock icon
Companies
Hint
Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

If multiple answers are possible, return any of them.

It is guaranteed that the length of the answer string is less than 104 for all the given inputs.

 

Example 1:

Input: numerator = 1, denominator = 2
Output: "0.5"
Example 2:

Input: numerator = 2, denominator = 1
Output: "2"
Example 3:

Input: numerator = 4, denominator = 333
Output: "0.(012)"
 

Constraints:

-231 <= numerator, denominator <= 231 - 1
denominator != 0
'''
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        digits = 10**4
        neg = (numerator < 0) ^ (denominator < 0)
        numerator = abs(numerator)
        denominator = abs(denominator)
        int_part = numerator // denominator
        rem = numerator % denominator
        if not rem:
            return str(int_part*(-1 if neg else 1))
        res = str(int_part) + '.'
        i = 0
        decimals = ''
        seen = {}
        while i < digits and rem:
            if rem in seen:
                repeat_start = seen[rem]
                non_repeating = decimals[:repeat_start]
                repeating = decimals[repeat_start:]
                ans = res + non_repeating + '(' + repeating + ')'
                return '-'+ans if neg else ans

            seen[rem] = i
            rem *= 10
            decimals += str(rem // denominator)
            rem %= denominator
            i += 1
        
        return res + decimals if not neg else '-'+res+decimals
