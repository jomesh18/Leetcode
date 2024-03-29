'''
Fraction to Recurring Decimal

Solution
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
        if numerator == 0: return '0'
        ans = ''
        isNeg = (numerator > 0) ^ (denominator > 0)
        numerator, denominator = abs(numerator), abs(denominator)
        if numerator > denominator:
            q, r = divmod(numerator, denominator)
            ans += str(q)
            numerator = r
        if numerator: 
            ans += '.' if ans else '0.'
            numerator *= 10
            oldr = dict()
            while True:
                while numerator < denominator:
                    ans += '0'
                    numerator *= 10
                q, r = divmod(numerator, denominator)
                ans += str(q)
                if r == 0:
                    break
                elif r in oldr:
                    p = oldr[r]
                    ans = ans[:p]+'('+ans[p:]+')'
                    break
                oldr[r] = len(ans)
                numerator = r*10
        return ans if not isNeg else '-'+ans

class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        sign = (numerator > 0) ^ (denominator > 0) if numerator else 0
        n, d = abs(numerator), abs(denominator)
        q, r = divmod(n, d)
        ans = str(q) if not r else str(q)+'.'
        n = r*10
        rems = {}
        while n:
            q, r = divmod(n, d)
            ans += str(q)
            if r == 0: break
            elif r in rems:
                pos = rems[r]
                ans = ans[:pos]+'('+ans[pos:]+')'
                break
            rems[r] = len(ans)
            n = r*10
        return ans if not sign else '-'+ans
            

class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        sign = (numerator > 0) ^ (denominator > 0) if numerator else 0
        n, d = abs(numerator), abs(denominator)
        q, r = divmod(n, d)
        ans = str(q) if not r else str(q)+'.'
        rems = {}
        while r>0 and r not in rems:
            rems[r] = len(ans)
            q, r = divmod(r*10, d)
            ans += str(q)
        if r in rems:
            pos = rems[r]
            ans = ans[:pos] + '(' + ans[pos:] + ')'
        return ans if not sign else '-'+ans
            