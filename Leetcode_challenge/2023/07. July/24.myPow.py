'''
50. Pow(x, n)
Medium

7928

7963

Add to List

Share
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

 

Example 1:

Input: x = 2.00000, n = 10
Output: 1024.00000
Example 2:

Input: x = 2.10000, n = 3
Output: 9.26100
Example 3:

Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
 

Constraints:

-100.0 < x < 100.0
-231 <= n <= 231-1
n is an integer.
Either x is not zero or n > 0.
-104 <= xn <= 104
'''
class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        memo = {}
        def helper(x1, n1):
            # print(n1)
            if n1 == 0: return 1
            if (x1, n1) in memo: return memo[(x1, n1)]
            ans = helper(x1, n1//2)
            ans *= ans
            if n1 & 1:
                ans *= x1
            memo[(x1, n1)] = ans
            return ans
        n1 = n
        if n < 0:
            n = -n
        ans = helper(x, n)
        return ans if n1 >= 0 else 1/ans