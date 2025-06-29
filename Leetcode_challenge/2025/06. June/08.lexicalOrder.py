'''
386. Lexicographical Numbers
Solved
Medium
Topics
premium lock icon
Companies
Given an integer n, return all the numbers in the range [1, n] sorted in lexicographical order.

You must write an algorithm that runs in O(n) time and uses O(1) extra space. 

 

Example 1:

Input: n = 13
Output: [1,10,11,12,13,2,3,4,5,6,7,8,9]
Example 2:

Input: n = 2
Output: [1,2]
 

Constraints:

1 <= n <= 5 * 104
'''
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = []
        def generate(res, n, curr):
            if not curr:
                start = 1
            else:
                start = 0
            for i in range(start, 10):
                new = curr*10+i
                if new > n:
                    break
                res.append(new)
                generate(res, n, new)
        generate(res, n, 0)
        return res