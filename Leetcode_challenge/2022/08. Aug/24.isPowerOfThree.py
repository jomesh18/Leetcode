'''
326. Power of Three
Easy

1605

159

Add to List

Share
Given an integer n, return true if it is a power of three. Otherwise, return false.

An integer n is a power of three, if there exists an integer x such that n == 3x.

 

Example 1:

Input: n = 27
Output: true
Example 2:

Input: n = 0
Output: false
Example 3:

Input: n = 9
Output: true
 

Constraints:

-231 <= n <= 231 - 1
 

Follow up: Could you solve it without loops/recursion?
Accepted
537,987
Submissions
1,207,679
'''
#iterative, log n
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1: return False
        while n != 1:
            if n % 3: return False
            n //= 3
        return True
            
# recursive
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1: return True
        if n < 1 or n % 3: return False
        return self.isPowerOfThree(n//3)

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        max_int = ((2**32)//2)-1
        max_power = int(log(max_int)//log(3))
        max_val = 3 ** max_power
        print(max_int, max_power, max_val)
        return n >= 1 and max_val % n == 0