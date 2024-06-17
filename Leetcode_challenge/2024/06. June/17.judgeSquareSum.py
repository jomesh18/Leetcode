'''
633. Sum of Square Numbers
Medium

2727

565

Add to List

Share
Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.

 

Example 1:

Input: c = 5
Output: true
Explanation: 1 * 1 + 2 * 2 = 5
Example 2:

Input: c = 3
Output: false
 

Constraints:

0 <= c <= 231 - 1
'''
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        d = set()
        for i in range(int(c**.5)+1):
            sq = i * i
            if c-sq in d or 2*sq == c:
                return True
            d.add(sq)
        return False


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for a in range(int(c**.5)+1):
            b_sq = c - a * a
            b = int(b_sq**0.5)
            if b * b == b_sq: return True
        return False


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l, r = 0, int(c**.5)
        while l <= r:
            a, b = l*l, r*r
            if (a + b) < c: l += 1
            elif (a + b) > c: r -= 1
            else: return True
        return False