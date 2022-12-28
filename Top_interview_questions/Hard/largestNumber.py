'''
179. Largest Number
Medium

6209

518

Add to List

Share
Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

Since the result may be very large, so you need to return a string instead of an integer.

 

Example 1:

Input: nums = [10,2]
Output: "210"
Example 2:

Input: nums = [3,30,34,5,9]
Output: "9534330"
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 109
'''
# O(n*n), O(1)
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if not (any(nums)): return '0'
        nums = [str(i) for i in nums]
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j] < nums[j] + nums[i]:
                    nums[i], nums[j] = nums[j], nums[i]
        return ''.join(nums)

# quick sort, O(nlogn), O(1)
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if not any(nums): return '0'
        n = len(nums)
        nums = [str(i) for i in nums]
        
        def partition(nums, l, r):
            pivot = random.randint(l, r)
            nums[r], nums[pivot] = nums[pivot], nums[r]
            pos = l
            for i in range(l, r):
                if nums[i]+nums[r] > nums[r]+nums[i]:
                    nums[pos], nums[i] = nums[i], nums[pos]
                    pos += 1
            nums[pos], nums[r] = nums[r], nums[pos]
            return pos
        
        def quick_sort(nums, l, r):
            if l >= r: return
            pos = partition(nums, l, r)
            quick_sort(nums, l, pos-1)
            quick_sort(nums, pos+1, r)

        quick_sort(nums, 0, n-1)
        return ''.join(nums)