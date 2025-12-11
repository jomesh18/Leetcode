'''
3583. Count Special Triplets
Solved
Medium
Topics
premium lock icon
Companies
Hint
You are given an integer array nums.

A special triplet is defined as a triplet of indices (i, j, k) such that:

0 <= i < j < k < n, where n = nums.length
nums[i] == nums[j] * 2
nums[k] == nums[j] * 2
Return the total number of special triplets in the array.

Since the answer may be large, return it modulo 109 + 7.

 

Example 1:

Input: nums = [6,3,6]

Output: 1

Explanation:

The only special triplet is (i, j, k) = (0, 1, 2), where:

nums[0] = 6, nums[1] = 3, nums[2] = 6
nums[0] = nums[1] * 2 = 3 * 2 = 6
nums[2] = nums[1] * 2 = 3 * 2 = 6
Example 2:

Input: nums = [0,1,0,0]

Output: 1

Explanation:

The only special triplet is (i, j, k) = (0, 2, 3), where:

nums[0] = 0, nums[2] = 0, nums[3] = 0
nums[0] = nums[2] * 2 = 0 * 2 = 0
nums[3] = nums[2] * 2 = 0 * 2 = 0
Example 3:

Input: nums = [8,4,2,8,4]

Output: 2

Explanation:

There are exactly two special triplets:

(i, j, k) = (0, 1, 3)
nums[0] = 8, nums[1] = 4, nums[3] = 8
nums[0] = nums[1] * 2 = 4 * 2 = 8
nums[3] = nums[1] * 2 = 4 * 2 = 8
(i, j, k) = (1, 2, 4)
nums[1] = 4, nums[2] = 2, nums[4] = 4
nums[1] = nums[2] * 2 = 2 * 2 = 4
nums[4] = nums[2] * 2 = 2 * 2 = 4
 

Constraints:

3 <= n == nums.length <= 105
0 <= nums[i] <= 105
'''
class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7
        num_set = set(nums)
        cands = set()
        for num in num_set:
            if num * 2 in num_set and num != 0:
                cands.add(num)
        ans = 0
        if 0 in num_set:
            count = nums.count(0)
            if count > 2:
                for i in range(1, count-1):
                    ans = (ans + i * (count-1-i))% MOD
        pos = {}
        for i, num in enumerate(nums):
            if (not (num & 1)) and num//2 in cands:
                if num//2 not in pos:
                    pos[num//2] = []
                pos[num//2].append(i)
        
        for i, num in enumerate(nums):
            if num not in cands: continue
            l = len(pos[num])
            if l < 2: continue
            j = bisect_left(pos[num], i)
            if j == l or j == 0: continue
            ans = (ans + j*(l-j)) % MOD
        return ans
