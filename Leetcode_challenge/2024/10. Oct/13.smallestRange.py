'''
632. Smallest Range Covering Elements from K Lists
Hard

4033

93

Add to List

Share
You have k lists of sorted integers in non-decreasing order. Find the smallest range that includes at least one number from each of the k lists.

We define the range [a, b] is smaller than range [c, d] if b - a < d - c or a < c if b - a == d - c.

 

Example 1:

Input: nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
Output: [20,24]
Explanation: 
List 1: [4, 10, 15, 24,26], 24 is in range [20,24].
List 2: [0, 9, 12, 20], 20 is in range [20,24].
List 3: [5, 18, 22, 30], 22 is in range [20,24].
Example 2:

Input: nums = [[1,2,3],[1,2,3],[1,2,3]]
Output: [1,1]
 

Constraints:

nums.length == k
1 <= k <= 3500
1 <= nums[i].length <= 50
-105 <= nums[i][j] <= 105
nums[i] is sorted in non-decreasing order.
'''
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        pq = []
        curr_max = nums[0][0]
        max_ij = (0, 0)
        for i in range(len(nums)):
            heappush(pq, (nums[i][0], i, 0))
            if nums[i][0] > curr_max:
                curr_max = nums[i][0]
                max_ij = (i, 0)
        a, b = pq[0][0], curr_max
        while pq:
            e, i, j = heappop(pq)
            if curr_max-e < b - a:
                a, b = e, curr_max
            if j + 1 == len(nums[i]):
                break
            curr_num = nums[i][j+1]
            if curr_num > curr_max:
                curr_max = curr_num
                max_ij = (i, j+1)
            heappush(pq, (curr_num, i, j+1))
        return [a, b]