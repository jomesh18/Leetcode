'''
Sqrt(x)

Solution
Given a non-negative integer x, compute and return the square root of x.

Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.

Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.

 

Example 1:

Input: x = 4
Output: 2
Example 2:

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned.
 

Constraints:

0 <= x <= 231 - 1
'''

# class Solution:
#     def mySqrt(self, x: int) -> int:
#         left, right, mid = 0, x+1, 0
#         while left < right:
#             mid = (left+right)>>1
#             if mid*mid == x:
#                 return mid
#             elif x < mid*mid:
#                 right = mid
#             elif x > mid*mid:
#                 left = mid+1
#         if mid*mid < x:
#             return mid
#         return mid-1

#from leetcode
class Solution(object):
    def mySqrt(self, x):
        l, r = 0, x
        while l <= r:
            mid = l + (r-l)//2
            if mid * mid <= x < (mid+1)*(mid+1):
                return mid
            elif x < mid * mid:
                r = mid - 1
            else:
                l = mid + 1

x = 4
# Output: 2
x = 8
# Output: 2

s = Solution()
print(s.mySqrt(x))
