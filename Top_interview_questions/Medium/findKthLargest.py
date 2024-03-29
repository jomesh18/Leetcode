'''
Kth Largest Element in an Array

Solution
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

You must solve it in O(n) time complexity.

 

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
 

Constraints:

1 <= k <= nums.length <= 105
-104 <= nums[i] <= 104
'''
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        heap = []
        for num in nums:
            if len(heap) == k:
                if num > heap[0]:
                    heappushpop(heap, num)
            else:
                heappush(heap, num)
        return heap[0]
        
#quick select O(n)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums: return 
        pivot = random.choice(nums)
        greater_than_pivot = [x for x in nums if x > pivot]
        equal_to_pivot = [x for x in nums if x == pivot]
        less_than_pivot = [x for x in nums if x < pivot]

        greater_len, equal_len = len(greater_than_pivot), len(equal_to_pivot)
        if k <= greater_len:
            return self.findKthLargest(greater_than_pivot, k)
        elif k > greater_len + equal_len:
            return self.findKthLargest(less_than_pivot, k-greater_len-equal_len)
        else:
            return equal_to_pivot[0]
        