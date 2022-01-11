'''
1009. Complement of Base 10 Integer
Easy

920

60

Add to List

Share
The complement of an integer is the integer you get when you flip all the 0's to 1's and all the 1's to 0's in its binary representation.

For example, The integer 5 is "101" in binary and its complement is "010" which is the integer 2.
Given an integer n, return its complement.

 

Example 1:

Input: n = 5
Output: 2
Explanation: 5 is "101" in binary, with complement "010" in binary, which is 2 in base-10.
Example 2:

Input: n = 7
Output: 0
Explanation: 7 is "111" in binary, with complement "000" in binary, which is 0 in base-10.
Example 3:

Input: n = 10
Output: 5
Explanation: 10 is "1010" in binary, with complement "0101" in binary, which is 5 in base-10.
 

Constraints:

0 <= n < 109
 
'''
class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0: return 1
        mask = n
        mask |= mask >> 1
        mask |= mask >> 2
        mask |= mask >> 4
        mask |= mask >> 8
        mask |= mask >> 16
        return mask ^ n

# N + bitwiseComplement(N) = 11....11 = X
# Then bitwiseComplement(N) = X - N
class Solution:
    def bitwiseComplement(self, n: int) -> int:
        x = 1
        while n > x:
            x = x*2+1
        return x-n

# N ^ bitwiseComplement(N) = 11....11 = X
# bitwiseComplement(N) = N ^ X
class Solution:
    def bitwiseComplement(self, n: int) -> int:
        x = 1
        while n > x:
            x = x*2 + 1
        return n^x
