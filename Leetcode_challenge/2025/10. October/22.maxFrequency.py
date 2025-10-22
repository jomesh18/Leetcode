'''
3347. Maximum Frequency of an Element After Performing Operations II
Solved
Hard
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

Adding 0 to nums[1], after which nums becomes [1, 4, 5].
Adding -1 to nums[2], after which nums becomes [1, 4, 4].
Example 2:

Input: nums = [5,11,20,20], k = 5, numOperations = 1

Output: 2

Explanation:

We can achieve a maximum frequency of two by:

Adding 0 to nums[1].
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 109
0 <= k <= 109
0 <= numOperations <= nums.length
 

'''
class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        nums.sort()
        count = Counter(nums)
        n = len(nums)
        l, r = 0, 0
        ans = 0
        for mid in range(n):
            while nums[mid] - nums[l] > k:
                l += 1
            while r+1 < n and nums[r+1] - nums[mid] <= k:
                r += 1
            ans = max(ans, min(r-l+1, numOperations+count[nums[mid]]))
        
        l = 0
        for r in range(n):
            mid = nums[l] + (nums[r]-nums[l])//2
            while mid - nums[l] > k or nums[r] - mid > k:
                l += 1
                mid = nums[l] + (nums[r]-nums[l])//2
            ans = max(ans, min(r-l+1, numOperations))
            
        return ans
