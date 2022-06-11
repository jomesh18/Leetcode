'''
1658. Minimum Operations to Reduce X to Zero
Medium

2334

42

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
Accepted
62,216
Submissions
177,686
'''
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)
        presum = [0]+list(accumulate(nums))
        # print(presum)
        max_len = 0
        l, r = 0, 0
        target = sum(nums) - x
        if target < 0: return -1
        if target == 0: return n
        s = 0
        #find max length sub array with sum = sum(nums)-x
        while r < n:
            # print(l, r, s)
            s = (presum[r+1]-presum[l])
            if s == target:
                max_len = max(max_len, r-l+1)
                r += 1
                l += 1
            elif s < target:
                r += 1
            else:
                l += 1
        return -1 if max_len == 0 else n-max_len


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)
        max_len = 0
        l, r = 0, 0
        target = sum(nums) - x
        if target < 0: return -1
        if target == 0: return n
        s = nums[0]
        #find max length sub array with sum = sum(nums)-x
        while r < n:
            # print(l, r, s)
            if s == target:
                max_len = max(max_len, r-l+1)
                s -= nums[l]
                r += 1
                s += (nums[r] if r < n else 0)
                l += 1
            elif s < target:
                r += 1
                s += (nums[r] if r < n else 0)
            else:
                s -= nums[l]
                l += 1
        return -1 if max_len == 0 else n-max_len