'''
3640. Trionic Array II
Solved
Hard
Topics
premium lock icon
Companies
Hint
You are given an integer array nums of length n.

A trionic subarray is a contiguous subarray nums[l...r] (with 0 <= l < r < n) for which there exist indices l < p < q < r such that:

nums[l...p] is strictly increasing,
nums[p...q] is strictly decreasing,
nums[q...r] is strictly increasing.
Return the maximum sum of any trionic subarray in nums.

 

Example 1:

Input: nums = [0,-2,-1,-3,0,2,-1]

Output: -4

Explanation:

Pick l = 1, p = 2, q = 3, r = 5:

nums[l...p] = nums[1...2] = [-2, -1] is strictly increasing (-2 < -1).
nums[p...q] = nums[2...3] = [-1, -3] is strictly decreasing (-1 > -3)
nums[q...r] = nums[3...5] = [-3, 0, 2] is strictly increasing (-3 < 0 < 2).
Sum = (-2) + (-1) + (-3) + 0 + 2 = -4.
Example 2:

Input: nums = [1,4,2,7]

Output: 14

Explanation:

Pick l = 0, p = 1, q = 2, r = 3:

nums[l...p] = nums[0...1] = [1, 4] is strictly increasing (1 < 4).
nums[p...q] = nums[1...2] = [4, 2] is strictly decreasing (4 > 2).
nums[q...r] = nums[2...3] = [2, 7] is strictly increasing (2 < 7).
Sum = 1 + 4 + 2 + 7 = 14.
 

Constraints:

4 <= n = nums.length <= 105
-109 <= nums[i] <= 109
It is guaranteed that at least one trionic subarray exists.
'''
class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        n = len(nums)
        i = 1
        l = 0
        cands = []
        while i < n:
            while i < n and nums[i] > nums[i-1]:
                i += 1
            if i == n:
                break
            if nums[i] == nums[i-1] or i == l + 1:
                l = i
                i += 1
                continue
            p = i - 1
            while i < n and nums[i] < nums[i-1]:
                i += 1
            if i == n:
                break
            if nums[i] == nums[i-1] or i == p + 1:
                l = i
                i += 1
                continue
            q = i - 1
            while i < n and nums[i] > nums[i-1]:
                i += 1
            r = i
            cands.append((l, p, q, i-1))
            l = q

        # print(cands)
        pre_sum = [0]*(n+1)
        for i in range(n):
            pre_sum[i+1] = pre_sum[i] + nums[i]
        # print('pre_sum', pre_sum)
        ans = float('-inf')
        for l, p, q, r in cands:
            # print(l, p, q, r)
            max_sum_ending_at_p_minus_1, max_sum_starting_at_q_plus_1 = float('-inf'), float('-inf')
            for i in range(l, p):
                max_sum_ending_at_p_minus_1 = max(max_sum_ending_at_p_minus_1, pre_sum[p] - pre_sum[i])
            for i in range(q+1, r+1):
                max_sum_starting_at_q_plus_1 = max(max_sum_starting_at_q_plus_1, pre_sum[i+1] - pre_sum[q+1])
            # print('max_sum_ending_at_p_minus_1', max_sum_ending_at_p_minus_1)
            # print('max_sum_starting_at_q_plus_1', max_sum_starting_at_q_plus_1)
            curr_sum = pre_sum[q+1] - pre_sum[p] + max_sum_ending_at_p_minus_1 + max_sum_starting_at_q_plus_1
            # print('curr_sum', curr_sum)
            ans = max(ans, curr_sum)

        return ans
