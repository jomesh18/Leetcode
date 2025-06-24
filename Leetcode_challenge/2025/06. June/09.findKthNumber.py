'''
440. K-th Smallest in Lexicographical Order
Solved
Hard
Topics
premium lock icon
Companies
Given two integers n and k, return the kth lexicographically smallest integer in the range [1, n].

 

Example 1:

Input: n = 13, k = 2
Output: 10
Explanation: The lexicographical order is [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9], so the second smallest number is 10.
Example 2:

Input: n = 1, k = 1
Output: 1
 

Constraints:

1 <= k <= n <= 109

'''
class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        curr = 1
        k -= 1
        def find_steps(pre1, pre2, n):
            steps = 0
            while pre1 <= n:
                steps += min(n+1, pre2) - pre1
                pre1 *= 10
                pre2 *= 10
            return steps

        while k > 0:
            steps = find_steps(curr, curr+1, n)
            if steps <= k:
                k -= steps
                curr += 1
            else:
                k -= 1
                curr *= 10
        return curr
