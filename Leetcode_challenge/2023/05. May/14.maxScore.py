'''
1799. Maximize Score After N Operations
Hard

1422

97

Add to List

Share
You are given nums, an array of positive integers of size 2 * n. You must perform n operations on this array.

In the ith operation (1-indexed), you will:

Choose two elements, x and y.
Receive a score of i * gcd(x, y).
Remove x and y from nums.
Return the maximum score you can receive after performing n operations.

The function gcd(x, y) is the greatest common divisor of x and y.

 

Example 1:

Input: nums = [1,2]
Output: 1
Explanation: The optimal choice of operations is:
(1 * gcd(1, 2)) = 1
Example 2:

Input: nums = [3,4,6,8]
Output: 11
Explanation: The optimal choice of operations is:
(1 * gcd(3, 6)) + (2 * gcd(4, 8)) = 3 + 8 = 11
Example 3:

Input: nums = [1,2,3,4,5,6]
Output: 14
Explanation: The optimal choice of operations is:
(1 * gcd(1, 5)) + (2 * gcd(2, 4)) + (3 * gcd(3, 6)) = 1 + 4 + 9 = 14
 

Constraints:

1 <= n <= 7
nums.length == 2 * n
1 <= nums[i] <= 106
'''
class Solution:
    def maxScore(self, nums: List[int]) -> int:
        n = len(nums)
        gcd_ij = [[0]*n for _ in range(n)]
        def gcd(x, y):
            return gcd(y, x%y) if y else x
        for i in range(n):
            for j in range(n):
                gcd_ij[i][j] = gcd(nums[i], nums[j])
        
        self.ans = 0    
        mask = (1<<n)-1
        memo = {}
        
        def backtrack(i, mask):
            if mask == 0:
                return 0
            if (i, mask) in memo: return memo[(i, mask)]
            ans = 0
            for k in range(n):
                if mask & (1<<k):
                    mask ^= (1<<k)
                    for l in range(n):
                        if mask & (1<<l):
                            ans = max(ans, gcd_ij[k][l]*i + backtrack(i+1, mask ^ (1<<l)))
                    mask ^= (1<<k)
            memo[(i, mask)] = ans
            return ans
        return backtrack(1, mask)
