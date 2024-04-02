'''
992. Subarrays with K Different Integers
Hard

5829

93

Add to List

Share
Given an integer array nums and an integer k, return the number of good subarrays of nums.

A good array is an array where the number of different integers in that array is exactly k.

For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.
A subarray is a contiguous part of an array.

 

Example 1:

Input: nums = [1,2,1,2,3], k = 2
Output: 7
Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2]
Example 2:

Input: nums = [1,2,1,3,4], k = 3
Output: 3
Explanation: Subarrays formed with exactly 3 different integers: [1,2,1,3], [2,1,3], [1,3,4].
 

Constraints:

1 <= nums.length <= 2 * 104
1 <= nums[i], k <= nums.length
'''
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        l = 0
        total_count = 0
        count = defaultdict(int)
        curr_count = 0
        for r, num in enumerate(nums):
            count[num] += 1
            if count[num] == 1:
                k -= 1
                if k < 0:
                    count[nums[l]] -= 1
                    k += 1
                    l += 1
                    curr_count = 0
            if k == 0:
                while count[nums[l]] > 1:
                    count[nums[l]] -= 1
                    l += 1
                    curr_count += 1
                total_count += curr_count + 1

        return total_count