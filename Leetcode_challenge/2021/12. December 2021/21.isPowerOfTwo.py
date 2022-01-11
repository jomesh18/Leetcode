'''
231. Power of Two
Easy

2364

260

Add to List

Share
Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2x.

 

Example 1:

Input: n = 1
Output: true
Explanation: 20 = 1
Example 2:

Input: n = 16
Output: true
Explanation: 24 = 16
Example 3:

Input: n = 3
Output: false
 

Constraints:

-231 <= n <= 231 - 1
 

Follow up: Could you solve it without loops/recursion?
'''
# using loops
# class Solution:
#     def isPowerOfTwo(self, n: int) -> bool:
#         if n <= 0: return False
#         while n != 1:
#             if n&1: return False
#             n >>= 1
#         return True

# #using recursion
# class Solution:
#     def isPowerOfTwo(self, n: int) -> bool:
#         if n <= 0: return False
#         if n == 1: return True
#         if n & 1: return False
#         return self.isPowerOfTwo(n>>1)

#without loop or recursion
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<=0: return False
        return not (n & (n-1))

n = 1
# Output: true

# n = 16
# Output: true

n = 3
# # Output: false

# n = 2**31

# n == -2

# n = -2**31

# # n = -2147483648


sol = Solution()
print(sol.isPowerOfTwo(n))
