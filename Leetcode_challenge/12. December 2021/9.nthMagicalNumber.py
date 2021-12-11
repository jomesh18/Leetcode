'''
878. Nth Magical Number
Hard

A positive integer is magical if it is divisible by either a or b.

Given the three integers n, a, and b, return the nth magical number. Since the answer may be very large, return it modulo 109 + 7.

 

Example 1:

Input: n = 1, a = 2, b = 3
Output: 2

Example 2:

Input: n = 4, a = 2, b = 3
Output: 6

Example 3:

Input: n = 5, a = 2, b = 4
Output: 10

Example 4:

Input: n = 3, a = 6, b = 4
Output: 8

 

Constraints:

    1 <= n <= 109
    2 <= a, b <= 4 * 104

Accepted
19,904
Submissions
59,982
'''
# https://leetcode.com/problems/nth-magical-number/discuss/1622471/C%2B%2B-Simple-Solution-w-Explanation-or-Brute-Force-%2B-Binary-Search-%2B-Math

#brute force, O(n*min(a,b))
#tle
# class Solution:
#     def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
#         mod = 10**9+7
#         i = min(a, b)
#         while n:
#             if i%a==0 or i%b==0:
#                 n -= 1
#             i += 1
#         return (i-1)%mod

#binary search O(log(n*min(a, b)))
#accepted
# from math import gcd
# class Solution:
#     def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
#         def enough(x):
#             lcm = a*b//gcd(a, b)
#             return (x//a) + (x//b) - (x//lcm)

#         mod = 10**9+7
#         lo, hi = min(a, b), n*min(a, b)
#         while lo < hi:
#             mid = lo + ((hi-lo)>>1)
#             if enough(mid) < n:
#                 lo = mid + 1
#             else:
#                 hi = mid
#         return lo%mod


#math solution
from math import gcd
class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        mod = 10**9+7
        l = (a*b)//gcd(a, b)
        c = l//a + l//b - 1
        k = (n-1) * c
        more_needed = n - k*c
        i, j = 1, 1
        ans = min(a, b)
        while more_needed:
            if i*a< j*b:
                ans = i*a
                i += 1
            else:
                ans = j*a
                j += 1
            more_needed -= 1
        return (k*l + ans) % mod

n = 1
a = 2
b = 3
# Output: 2

# n = 4
# a = 2
# b = 3
# # Output: 6

# # n = 5
# # a = 2
# # b = 4
# # # Output: 10

# # n = 3
# # a = 6
# # b = 4
# Output: 8

sol = Solution()
print(sol.nthMagicalNumber(n, a, b))
