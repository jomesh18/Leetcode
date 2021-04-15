'''
Pow(x, n)

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
# class Solution:
#     def myPow(self, x: float, n: int) -> float:
#         return x**n

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0: return 1
        temp = self.myPow(x, int(n/2))
        ans = temp * temp
        if n > 0 and n%2 != 0:
            ans *= x
        if n<0 and n%2 != 0:
            ans /= x
        return ans

#from leetcode iterative using binary exponentiation, ref below
#https://cp-algorithms.com/algebra/binary-exp.html
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n<0:
            x = 1/x
            n = -n
        res = 1
        while n:
            if x & 1:
                res *= x
            x *= x
            n >>= 1
        return res

#from leetcode, recursive
class Solution:
    def myPow(self, x, n):
        if not n:
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)
        if n % 2:
            return x * self.myPow(x, n-1)
        return self.myPow(x*x, n/2)

# x = 2.00000
# n = 10
# # Output: 1024.00000
# x = 2.10000
# n = 3
# # Output: 9.26100
# x = 2.00000
# n = -2
# # Output: 0.25000
x = 2.00000
n = -3
# Output: 0.125000
s = Solution()
print(s.myPow(x, n))
