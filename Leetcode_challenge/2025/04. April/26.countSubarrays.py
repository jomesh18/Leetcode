'''
2444. Count Subarrays With Fixed Bounds
Solved
Hard
Topics
premium lock icon
Companies
Hint
You are given an integer array nums and two integers minK and maxK.

A fixed-bound subarray of nums is a subarray that satisfies the following conditions:

The minimum value in the subarray is equal to minK.
The maximum value in the subarray is equal to maxK.
Return the number of fixed-bound subarrays.

A subarray is a contiguous part of an array.

 

Example 1:

Input: nums = [1,3,5,2,7,5], minK = 1, maxK = 5
Output: 2
Explanation: The fixed-bound subarrays are [1,3,5] and [1,3,5,2].
Example 2:

Input: nums = [1,1,1,1], minK = 1, maxK = 1
Output: 10
Explanation: Every subarray of nums is a fixed-bound subarray. There are 10 possible subarrays.
 

Constraints:

2 <= nums.length <= 105
1 <= nums[i], minK, maxK <= 106
'''
class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        n = len(nums)
        ans = 0
        pos = []
        for i in range(n):
            if nums[i] > maxK or nums[i] < minK:
                pos.append(i)

        def find(s, e):
            ans = 0
            min_pos, max_pos = [], []
            for i in range(s, e):
                if nums[i] == minK:
                    min_pos.append(i)
                if nums[i] == maxK:
                    max_pos.append(i)
            
            i, j = 0, 0
            for k in range(s, e):
                while i < len(min_pos) and min_pos[i] < k:
                    i += 1
                while j < len(max_pos) and max_pos[j] < k:
                    j += 1
                if i == len(min_pos) or j == len(max_pos):
                    break
                ans += e - max(min_pos[i], max_pos[j])
                
            return ans

        l = 0
        for i in range(len(pos)):
            r = pos[i]
            ans += find(l, r)
            l = r+1
        
        ans += find(l, n)
        return ans
            