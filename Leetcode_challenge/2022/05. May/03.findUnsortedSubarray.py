'''
581. Shortest Unsorted Continuous Subarray
Medium

6271

226

Add to List

Share
Given an integer array nums, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order.

Return the shortest such subarray and output its length.

 

Example 1:

Input: nums = [2,6,4,8,10,9,15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
Example 2:

Input: nums = [1,2,3,4]
Output: 0
Example 3:

Input: nums = [1]
Output: 0
 

Constraints:

1 <= nums.length <= 104
-105 <= nums[i] <= 105
 

Follow up: Can you solve it in O(n) time complexity?
Accepted
262,148
Submissions
731,021
'''
#O(n*n) #tle
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        r, l = 0, len(nums)
        
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[j] < nums[i]:
                    r = max(r, j)
                    l = min(l, i)
        
        return r-l+1

#O(nlogn) sorting, accepted
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        l, r = len(nums)-1, 0
        
        a = nums[:]
        a.sort()
        for i in range(len(a)):
            if a[i] != nums[i]:
                l = min(l, i)
                r = max(r, i)

        return r-l+1 if r else 0

#O(n) time, O(n) space
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        l, r = len(nums)-1, 0
        
        stack = []
        
        for i, num in enumerate(nums):
            while stack and nums[stack[-1]] > num:
                l = min(stack.pop(), l)
            stack.append(i)
        stack = []
        for i in range(len(nums)-1, -1, -1):
            while stack and nums[stack[-1]] < nums[i]:
                r = max(stack.pop(), r)
            stack.append(i)
            
        return r-l+1 if r-l > 0 else 0

#O(n) time, O(1) space
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        
        min__, max__ = float('inf'), float("-inf")
        
        flag = False
        
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                flag = True
            if flag:
                min__ = min(min__, nums[i])
        
        flag = False
        for i in range(len(nums)-2, -1, -1):
            if nums[i+1] < nums[i]:
                flag = True
            if flag:
                max__ = max(max__, nums[i])
        
        l, r = len(nums), 0
        for i in range(len(nums)):
            if min__ < nums[i]:
                l = i
                break
        for i in range(len(nums)-1, -1, -1):
            if max__ > nums[i]:
                r = i
                break
                
        return r-l+1 if r-l > 0 else 0