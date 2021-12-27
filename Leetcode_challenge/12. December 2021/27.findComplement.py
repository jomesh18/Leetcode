'''
476. Number Complement
Easy

1546

94

Add to List

Share
The complement of an integer is the integer you get when you flip all the 0's to 1's and all the 1's to 0's in its binary representation.

For example, The integer 5 is "101" in binary and its complement is "010" which is the integer 2.
Given an integer num, return its complement.

 

Example 1:

Input: num = 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.
Example 2:

Input: num = 1
Output: 0
Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.
 

Constraints:

1 <= num < 231
 

Note: This question is the same as 1009: https://leetcode.com/problems/complement-of-base-10-integer/
'''
# class Solution:
#     def findComplement(self, num: int) -> int:

#         bit_length = len(bin(num))-2
#         return num ^ int('1'*bit_length, 2)

class Solution:
    def findComplement(self, num: int) -> int:
        i = 1
        while i<=num:
            i <<= 1
        return (i-1) ^ num

class Solution:
    def findComplement(self, num: int) -> int:
        mask = num
        mask |= mask >> 1
        mask |= mask >> 2
        mask |= mask >> 4
        mask |= mask >> 8
        mask |= mask >> 16
        return mask ^ num

class Solution:
     def findComplement(self, num):
            return num ^ ((1<<num.bit_length())-1)