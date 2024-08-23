'''
264. Ugly Number II
Medium

6504

393

Add to List

Share
An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

Given an integer n, return the nth ugly number.

 

Example 1:

Input: n = 10
Output: 12
Explanation: [1, 2, 3, 4, 5, 6, 8, 9, 10, 12] is the sequence of the first 10 ugly numbers.
Example 2:

Input: n = 1
Output: 1
Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.
 

Constraints:

1 <= n <= 1690
'''
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n == 1: return 1
        heap = [1]
        removed = 0
        while removed < n-1:
            curr = heappop(heap)
            while heap and heap[0] == curr:
                heappop(heap)
            removed += 1
            for num in [2, 3, 5]:
                heappush(heap, curr*num)
        return heappop(heap)
        