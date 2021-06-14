'''
Pow(x, n)

Solution
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
-104 <= xn <= 104
'''

#my try, iterative
# class Solution:
#     def myPow(self, x: float, n: int) -> float:
#         if n == 0: return 1
#         ans = x
#         prev = 1
#         if n < 0:
#             ans = 1/x
#             n = -n
#         while n!= 1:
#             if n%2 == 1:
#                 prev *= ans
#             ans *= ans
#             n = n>>1
#         return prev*ans

#from leetcode, iterative
class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = 1
        absn = abs(n)
        while absn > 0:
            print(absn, ans, x)
            if absn & 1 == 1:
                ans *= x
            absn >>= 1
            x *= x
        return 1/ans if n < 0 else ans

#my try, recursive
# class Solution:
#     def myPow(self, x: float, n: int) -> float:
#         if n < 0:
#             x = 1/x
#             n = -n
#         def helper(x, n):
#             if n == 0:
#                 return 1
#             if n%2 != 0:
#                 return x * helper(x*x, n>>1)
#             else:
#                 return helper(x*x, n>>1)
#         return helper(x, n)

#from leetcode, recursive
class Solution:
    def myPow(self, x, n):
        if abs(x) < 1e-40: return 0 
        if n == 0: return 1
        if n < 0: return self.myPow(1/x, -n)
        lower = self.myPow(x, n//2)
        return lower*lower*x if n&1 else lower*lower

x = 2.00000
n = 10
# Output: 1024.00000
# x = 2.10000
# n = 3
# # Output: 9.26100
# x = 2.00000
# n = -2
# Output: 0.25000
s = Solution()
print(s.myPow(x, n))
