'''
1248. Count Number of Nice Subarrays
Medium

4064

89

Add to List

Share
Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.

Return the number of nice sub-arrays.

 

Example 1:

Input: nums = [1,1,2,1,1], k = 3
Output: 2
Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].
Example 2:

Input: nums = [2,4,6], k = 1
Output: 0
Explanation: There are no odd numbers in the array.
Example 3:

Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
Output: 16
 

Constraints:

1 <= nums.length <= 50000
1 <= nums[i] <= 10^5
1 <= k <= nums.length
'''
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        odd_count, nice, l, last = 0, 0, 0, -1
        for r in range(len(nums)):
            while l <= r and not (nums[l] & 1):
                l += 1
            if nums[r] & 1:
                odd_count += 1
            if odd_count == k:
                nice += l - last
            elif odd_count > k:
                last = l
                l += 1
                odd_count -= 1
                while l <= r and not (nums[l] & 1):
                    l += 1
                nice += l - last
                
        return nice
