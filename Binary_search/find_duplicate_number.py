'''
Find the Duplicate Number

Solution
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.

 

Example 1:

Input: nums = [1,3,4,2,2]
Output: 2
Example 2:

Input: nums = [3,1,3,4,2]
Output: 3
Example 3:

Input: nums = [1,1]
Output: 1
Example 4:

Input: nums = [1,1,2]
Output: 1
 

Constraints:

1 <= n <= 105
nums.length == n + 1
1 <= nums[i] <= n
All the integers in nums appear only once except for precisely one integer which appears two or more times.
 

Follow up:

How can we prove that at least one duplicate number must exist in nums?
Can you solve the problem in linear runtime complexity?
'''
#from leetcode, Floyd's algorithm
class Solution:
    def findDuplicate(self, nums: [int]) -> int:
        tortoise, hare = nums[0], nums[0]
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break
        tortoise = nums[0]
        while hare != tortoise:
            hare = nums[hare]
            tortoise = nums[tortoise]
        return tortoise

#from leetcode, binary search O(nlogn)
'''
There is Binary Search solution with time complexity O(n log n) and space complexity O(1). We have numbers from 1 to n. 
Let us choose middle element m = n//2 and count number of elements in list, which are less or equal than m. 
If we have m+1 of them it means we need to search for duplicate in [1,m] range, else in [m+1,n] range. 
Each time we reduce searching range twice, but each time we go over all data. So overall complexity is O(n log n).
'''
class Solution(object):
    def findDuplicate(self, nums):
        beg, end = 1, len(nums)-1
        
        while beg + 1 <= end:
            mid, count = (beg + end)//2, 0
            for num in nums:
                if num <= mid: count += 1        
            if count <= mid:
                beg = mid + 1
            else:
                end = mid
        return end
nums = [1,3,4,2,2]
# Output: 2

nums = [3,1,3,4,2]
# # Output: 3

nums = [1,1]
# # Output: 1

nums = [1,1,2]
# Output: 1

s = Solution()
print(s.findDuplicate(nums))
