'''
1802. Maximum Value at a Given Index in a Bounded Array
Medium

2229

355

Add to List

Share
You are given three positive integers: n, index, and maxSum. You want to construct an array nums (0-indexed) that satisfies the following conditions:

nums.length == n
nums[i] is a positive integer where 0 <= i < n.
abs(nums[i] - nums[i+1]) <= 1 where 0 <= i < n-1.
The sum of all the elements of nums does not exceed maxSum.
nums[index] is maximized.
Return nums[index] of the constructed array.

Note that abs(x) equals x if x >= 0, and -x otherwise.

 

Example 1:

Input: n = 4, index = 2,  maxSum = 6
Output: 2
Explanation: nums = [1,2,2,1] is one array that satisfies all the conditions.
There are no arrays that satisfy all the conditions and have nums[2] == 3, so 2 is the maximum nums[2].
Example 2:

Input: n = 6, index = 1,  maxSum = 10
Output: 3
 

Constraints:

1 <= n <= maxSum <= 109
0 <= index < n
'''
class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        
        def valid(val):
            if val <= index:
                left_sum = (val*(val+1)//2) + (index-val+1)
            else:
                left_sum = (index+1)*(2*val-index)//2
                
            terms_left = n-index
            if val > terms_left:
                right_sum = terms_left*((val-terms_left+1)+val)//2
            else:
                right_sum = (val*(val+1)//2) + (terms_left-val)
            
            # print(val, left_sum, right_sum)
            return (left_sum+right_sum-val) <= maxSum
            
        l, h = 1, maxSum+1
        ans = 1
        while l < h:
            mid = (l+h)//2
            if valid(mid):
                ans = mid
                l = mid + 1
            else:
                h = mid
        return ans