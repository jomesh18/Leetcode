'''
Search in a Sorted Array of Unknown Size
Given an integer array sorted in ascending order, write a function to searchtargetinnums. Iftargetexists, then return its index, otherwise return-1.However, the array size is unknown to you. You may only access the array using anArrayReader interface, where ArrayReader.get(k)returns the element of the array at indexk (0-indexed).

You may assume all integers in the array are less than 10000, and if you access the array out of bounds,ArrayReader.getwill return2147483647.

Example 1:

Input:
array
 = [-1,0,3,5,9,12], 
target
 = 9
​
Output:
 4
​
Explanation:
 9 exists in 
nums
 and its index is 4
Example 2:

Input:
array
 = [-1,0,3,5,9,12], 
target
 = 2
​
Output:
 -1
​
Explanation:
 2 does not exist in 
nums
 so return -1
Note:

You may assume that all elements in the array are unique.

The value of each element in the array will be in the range[-9999, 9999].

'''

'''
Suppose you have a sorted array of infinite numbers, how would you search an element in the array?
Source: Amazon Interview Experience. 
Since array is sorted, the first thing clicks into mind is binary search, but the problem here is that we don’t know size of array. 
If the array is infinite, that means we don’t have proper bounds to apply binary search. So in order to find position of key, first we find bounds and then apply binary search algorithm.
Let low be pointing to 1st element and high pointing to 2nd element of array, Now compare key with high index element, 
->if it is greater than high index element then copy high index in low index and double the high index. 
->if it is smaller, then apply binary search on high and low indices found'''

class Solution:
	def search(self, nums, target):
		if not nums: return -1
		if len(nums) == 1: return 0 if nums[0] == target else -1
		r = 1
		while nums[r] < target:
			r *= 2
		l = r//2
		while l < r:
			mid = l + ((r-l)>>1)
			if nums[mid] < target:
				l = mid + 1
			else:
				r = mid
		return l if nums[l] == target else -1

array = [-1,0,3,5,9,12]
target = 9
# Output: 4

array = [-1,0,3,5,9,12]
target= 2
# Output:-1

s = Solution()
print(s.search(array, target))