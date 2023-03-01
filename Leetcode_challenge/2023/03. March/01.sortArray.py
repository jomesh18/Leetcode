'''
912. Sort an Array
Medium

3782

640

Add to List

Share
Given an array of integers nums, sort the array in ascending order and return it.

You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.

 

Example 1:

Input: nums = [5,2,3,1]
Output: [1,2,3,5]
Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).
Example 2:

Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]
Explanation: Note that the values of nums are not necessairly unique.
 

Constraints:

1 <= nums.length <= 5 * 104
-5 * 104 <= nums[i] <= 5 * 104
'''
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(l, m, r):
            i, j = l, m+1
            t = []
            while i <= m and j <= r:
                if nums[i] < nums[j]:
                    t.append(nums[i])
                    i += 1
                else:
                    t.append(nums[j])
                    j += 1
            while i <= m:
                t.append(nums[i])
                i += 1
            while j <= r:
                t.append(nums[j])
                j += 1
            for i in range(l, r+1):
                nums[i] = t[i-l]
                    
        def merge_sort(start, end):
            if end > start:
                mid = (start+end)//2
                merge_sort(start, mid)
                merge_sort(mid+1, end)
                merge(start, mid, end)
        
        merge_sort(0, len(nums)-1)
        return nums