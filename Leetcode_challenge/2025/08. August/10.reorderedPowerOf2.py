'''
869. Reordered Power of 2
Solved
Medium
Topics
premium lock icon
Companies
You are given an integer n. We reorder the digits in any order (including the original order) such that the leading digit is not zero.

Return true if and only if we can do this so that the resulting number is a power of two.

 

Example 1:

Input: n = 1
Output: true
Example 2:

Input: n = 10
Output: false
 

Constraints:

1 <= n <= 109
'''
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        powers_of_two = set()
        curr = 1
        while curr <= 1e9:
            powers_of_two.add(''.join(sorted(str(curr))))
            curr <<= 1
        
        return ''.join(sorted(str(n))) in powers_of_two
