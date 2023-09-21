'''
1658. Minimum Operations to Reduce X to Zero
Medium

4489

90

Add to List

Share
You are given an integer array nums and an integer x. In one operation, you can either remove the leftmost or the rightmost element from the array nums and subtract its value from x. Note that this modifies the array for future operations.

Return the minimum number of operations to reduce x to exactly 0 if it is possible, otherwise, return -1.

 

Example 1:

Input: nums = [1,1,4,2,3], x = 5
Output: 2
Explanation: The optimal solution is to remove the last two elements to reduce x to zero.
Example 2:

Input: nums = [5,6,7,8,9], x = 4
Output: -1
Example 3:

Input: nums = [3,2,20,1,1,3], x = 10
Output: 5
Explanation: The optimal solution is to remove the last three elements and the first two elements (5 operations in total) to reduce x to zero.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 104
1 <= x <= 109
'''
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)
        target = sum(nums)-x
        if target < 0: return -1
        l = 0
        curr_sum = 0
        ans = float('inf')
        for r in range(n):
            curr_sum += nums[r]
            if curr_sum == target:
                ans = min(ans, n-(r-l+1))
            elif curr_sum > target:
                while curr_sum > target and l <= r:
                    curr_sum -= nums[l]
                    l += 1
                    if curr_sum == target:
                        ans = min(ans, n-(r-l+1))
            # print(r, curr_sum, l, ans)
        return ans if ans != float('inf') else -1