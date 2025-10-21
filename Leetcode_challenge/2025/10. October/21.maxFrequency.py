'''
3346. Maximum Frequency of an Element After Performing Operations I
Solved
Medium
Topics
premium lock icon
Companies
Hint
You are given an integer array nums and two integers k and numOperations.

You must perform an operation numOperations times on nums, where in each operation you:

Select an index i that was not selected in any previous operations.
Add an integer in the range [-k, k] to nums[i].
Return the maximum possible frequency of any element in nums after performing the operations.

 

Example 1:

Input: nums = [1,4,5], k = 1, numOperations = 2

Output: 2

Explanation:

We can achieve a maximum frequency of two by:

Adding 0 to nums[1]. nums becomes [1, 4, 5].
Adding -1 to nums[2]. nums becomes [1, 4, 4].
Example 2:

Input: nums = [5,11,20,20], k = 5, numOperations = 1

Output: 2

Explanation:

We can achieve a maximum frequency of two by:

Adding 0 to nums[1].
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 105
0 <= k <= 105
0 <= numOperations <= nums.length
'''
class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        nums.sort()
        count = {}
        last_ind = 0
        n = len(nums)
        for i in range(n):
            if nums[last_ind] != nums[i]:
                count[nums[last_ind]] = i-last_ind
                last_ind = i
        count[nums[last_ind]] = n - last_ind
        ans = max(count.values())
        for i in range(nums[0], nums[-1]+1):
            lo = bisect_left(nums, i-k)
            hi = bisect_right(nums, i+k) - 1
            if i not in count:
                curr = min(hi-lo+1, numOperations)
            else:
                curr = min(hi-lo+1, numOperations+count[i])
            ans = max(ans, curr)
        
        return ans
