'''
2429. Minimize XOR
Solved
Medium
Topics
Companies
Hint
Given two positive integers num1 and num2, find the positive integer x such that:

x has the same number of set bits as num2, and
The value x XOR num1 is minimal.
Note that XOR is the bitwise XOR operation.

Return the integer x. The test cases are generated such that x is uniquely determined.

The number of set bits of an integer is the number of 1's in its binary representation.

 

Example 1:

Input: num1 = 3, num2 = 5
Output: 3
Explanation:
The binary representations of num1 and num2 are 0011 and 0101, respectively.
The integer 3 has the same number of set bits as num2, and the value 3 XOR 3 = 0 is minimal.
Example 2:

Input: num1 = 1, num2 = 12
Output: 3
Explanation:
The binary representations of num1 and num2 are 0001 and 1100, respectively.
The integer 3 has the same number of set bits as num2, and the value 3 XOR 1 = 2 is minimal.
 

Constraints:

1 <= num1, num2 <= 109
'''
class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        def find_set_bits(num):
            set_bit_count = 0
            while num:
                if num & 1:
                    set_bit_count += 1
                num >>= 1
            return set_bit_count
        bits2 = find_set_bits(num2)
        bits1 = find_set_bits(num1)

        if bits2 == bits1:
            return num1
        if bits1 < bits2:
            diff = bits2 - bits1
            i = 0
            curr = num1
            while diff:
                while curr & (1<<i):
                    i += 1
                curr ^= (1<<i)
                i += 1
                diff -= 1
            return curr
        else:
            curr = 0
            i = len(bin(num1))-2
            i -= 1
            for _ in range(bits2):
                while not ((1<<i) & num1):
                    i -= 1
                curr ^= (1<<i)
                i -= 1
            return curr
