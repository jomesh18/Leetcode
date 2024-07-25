'''
912. Sort an Array
Medium

6207

777

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
        
        def merge_sort(l, r):
            if l < r:
                m = (l + r) // 2
                merge_sort(l, m)
                merge_sort(m+1, r)
                new = []
                i1, i2 = l, m+1
                while i1 <= m and i2 <= r:
                    if nums[i1] < nums[i2]:
                        new.append(nums[i1])
                        i1 += 1
                    else:
                        new.append(nums[i2])
                        i2 += 1
                while i1 <= m:
                    new.append(nums[i1])
                    i1 += 1
                while i2 <= r:
                    new.append(nums[i2])
                    i2 += 1
                for i in range(l, r+1):
                    nums[i] = new[i-l]
            
        merge_sort(0, len(nums)-1)
        return nums