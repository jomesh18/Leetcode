'''
461. Hamming Distance
Easy

2512

186

Add to List

Share
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, return the Hamming distance between them.

 

Example 1:

Input: x = 1, y = 4
Output: 2
Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑
The above arrows point to positions where the corresponding bits are different.
Example 2:

Input: x = 3, y = 1
Output: 1
 

Constraints:

0 <= x, y <= 231 - 1
Accepted
426,240
Submissions
577,992
'''
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        differed_bits = x ^ y
        count = 0
        for i in range(31):
            count += (differed_bits>>i) & 1
        return count