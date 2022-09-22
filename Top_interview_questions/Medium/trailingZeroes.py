'''
172. Factorial Trailing Zeroes
Medium

2254

1736

Add to List

Share
Given an integer n, return the number of trailing zeroes in n!.

Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.

 

Example 1:

Input: n = 3
Output: 0
Explanation: 3! = 6, no trailing zero.
Example 2:

Input: n = 5
Output: 1
Explanation: 5! = 120, one trailing zero.
Example 3:

Input: n = 0
Output: 0
 

Constraints:

0 <= n <= 104
 

Follow up: Could you write a solution that works in logarithmic time complexity?
'''
https://www.purplemath.com/modules/factzero.htm
class Solution:
    def trailingZeroes(self, n: int) -> int:
        zeroes = 0
        mul_of_five = 5
        while mul_of_five <= n:
            zeroes += n//mul_of_five
            mul_of_five *= 5
        return zeroes