'''
2163. Minimum Difference in Sums After Removal of Elements
Solved
Hard
Topics
premium lock icon
Companies
Hint
You are given a 0-indexed integer array nums consisting of 3 * n elements.

You are allowed to remove any subsequence of elements of size exactly n from nums. The remaining 2 * n elements will be divided into two equal parts:

The first n elements belonging to the first part and their sum is sumfirst.
The next n elements belonging to the second part and their sum is sumsecond.
The difference in sums of the two parts is denoted as sumfirst - sumsecond.

For example, if sumfirst = 3 and sumsecond = 2, their difference is 1.
Similarly, if sumfirst = 2 and sumsecond = 3, their difference is -1.
Return the minimum difference possible between the sums of the two parts after the removal of n elements.

 

Example 1:

Input: nums = [3,1,2]
Output: -1
Explanation: Here, nums has 3 elements, so n = 1. 
Thus we have to remove 1 element from nums and divide the array into two equal parts.
- If we remove nums[0] = 3, the array will be [1,2]. The difference in sums of the two parts will be 1 - 2 = -1.
- If we remove nums[1] = 1, the array will be [3,2]. The difference in sums of the two parts will be 3 - 2 = 1.
- If we remove nums[2] = 2, the array will be [3,1]. The difference in sums of the two parts will be 3 - 1 = 2.
The minimum difference between sums of the two parts is min(-1,1,2) = -1. 
Example 2:

Input: nums = [7,9,5,8,1,3]
Output: 1
Explanation: Here n = 2. So we must remove 2 elements and divide the remaining array into two parts containing two elements each.
If we remove nums[2] = 5 and nums[3] = 8, the resultant array will be [7,9,1,3]. The difference in sums will be (7+9) - (1+3) = 12.
To obtain the minimum difference, we should remove nums[1] = 9 and nums[4] = 1. The resultant array becomes [7,5,8,3]. The difference in sums of the two parts is (7+5) - (8+3) = 1.
It can be shown that it is not possible to obtain a difference smaller than 1.
 

Constraints:

nums.length == 3 * n
1 <= n <= 105
1 <= nums[i] <= 105
'''
class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums) // 3
        max_heap = [-num for num in nums[:n]]
        s = -sum(max_heap)
        min_sum = [float('inf')]*(3*n)
        min_sum[n-1] = s
        heapify(max_heap)
        for i in range(n, 3*n):
            if nums[i] < -max_heap[0]:
                s += nums[i] + max_heap[0]
                heappop(max_heap)
                heappush(max_heap, -nums[i])
            min_sum[i] = s
        max_sum = [float('-inf')]*(3*n)
        min_heap = [num for num in nums[2*n:]]
        s = sum(min_heap)
        max_sum[2*n] = s
        heapify(min_heap)
        for i in range(2*n-1, -1, -1):
            if nums[i] > min_heap[0]:
                s += nums[i] - min_heap[0]
                heappop(min_heap)
                heappush(min_heap, nums[i])
            max_sum[i] = s
        # print(n)
        # print(max_sum)
        # print(min_sum)
        ans = float('inf')
        for i in range(n-1, 2*n):
            ans = min(ans, min_sum[i]-max_sum[i+1])
        
        return ans
