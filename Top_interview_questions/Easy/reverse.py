'''
Reverse Integer

Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321

Example 2:

Input: x = -123
Output: -321

Example 3:

Input: x = 120
Output: 21

Example 4:

Input: x = 0
Output: 0

 

Constraints:

    -231 <= x <= 231 - 1

'''
class Solution:
    def reverse(self, x: int) -> int:
        ans = 0
        isNeg = False
        if x < 0: 
            isNeg = True
            x = -x
        while x:
            ans = ans * 10 + x%10
            x //= 10
            # print(ans, x)
        if ans >= 2**31: ans = 0
        if isNeg: ans *= -1
        return ans

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = [1,-1][x < 0]
        rst = sign * int(str(abs(x))[::-1])
        return rst if -(2**31)-1 < rst < 2**31 else 0

# x = 123
# Output: 321

x = -123
# Output: -321

x = 120
# Output: 21

# x = 0
# Output: 0

x = 1534236469

sol = Solution()
print(sol.reverse(x))
