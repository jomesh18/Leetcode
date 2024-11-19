'''
2461. Maximum Sum of Distinct Subarrays With Length K
Medium

1629

31

Add to List

Share
You are given an integer array nums and an integer k. Find the maximum subarray sum of all the subarrays of nums that meet the following conditions:

The length of the subarray is k, and
All the elements of the subarray are distinct.
Return the maximum subarray sum of all the subarrays that meet the conditions. If no subarray meets the conditions, return 0.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,5,4,2,9,9,9], k = 3
Output: 15
Explanation: The subarrays of nums with length 3 are:
- [1,5,4] which meets the requirements and has a sum of 10.
- [5,4,2] which meets the requirements and has a sum of 11.
- [4,2,9] which meets the requirements and has a sum of 15.
- [2,9,9] which does not meet the requirements because the element 9 is repeated.
- [9,9,9] which does not meet the requirements because the element 9 is repeated.
We return 15 because it is the maximum subarray sum of all the subarrays that meet the conditions
Example 2:

Input: nums = [4,4,4], k = 3
Output: 0
Explanation: The subarrays of nums with length 3 are:
- [4,4,4] which does not meet the requirements because the element 4 is repeated.
We return 0 because no subarrays meet the conditions.
 

Constraints:

1 <= k <= nums.length <= 105
1 <= nums[i] <= 105
'''
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        count = dict()
        s = 0
        duplicate = 0
        for i in range(len(nums)):
            if nums[i] in count and count[nums[i]] == 1:
                duplicate += 1
            count[nums[i]] = count.get(nums[i], 0) + 1
            s += nums[i]
            if i == k-1 and not duplicate:
                ans = max(ans, s)
            if i >= k:
                to_del = nums[i-k]
                count[to_del] -= 1
                if count[to_del] == 1:
                    duplicate -= 1
                s -= to_del
                if not duplicate:
                    ans = max(ans, s)
        return ans