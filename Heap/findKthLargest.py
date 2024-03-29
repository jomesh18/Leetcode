'''
215. Kth Largest Element in an Array
Medium

8325

459

Add to List

Share
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

 

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
 

Constraints:

1 <= k <= nums.length <= 104
-104 <= nums[i] <= 104
Accepted
1,203,510
Submissions
1,920,664
'''

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        l = nums[:k]
        heapq.heapify(l)
        for i in nums[k:]:
            if i > l[0]:
                heapq.heapreplace(l, i)
        return heapq.heappop(l)