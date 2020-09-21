# class Solution:
#     def rotate(self, nums: [int], k: int) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         for _ in range(k):
#         	nums.insert(0, nums.pop(len(nums)-1))

# nums = [1,2,3,4,5,6,7]
# k = 3
# print("nums before rotating: {}".format(nums))
# obj = Solution()
# obj.rotate(nums, k)
# print("nums after rotating: {}".format(nums))

# using cyclic replacement, from leetcode
# class Solution:
#     def rotate(self, nums: [int], k: int) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         n = len(nums)
#         k %= n
#         start = count = 0
#         while count < n:
#         	current = start
#         	prev = nums[current]
#         	while True:
#         		next_index = (current + k) % n
#         		nums[next_index], prev = prev, nums[next_index]
#         		current = next_index
#         		count += 1
#         		if current == start:
#         			break
#         	start += 1
				
# nums = [1,2,3,4,5,6,7]
# k = 3
# print("nums before rotating: {}".format(nums))
# obj = Solution()
# obj.rotate(nums, k)
# print("nums after rotating: {}".format(nums))

# reversal of array
class Solution:
	def reverse_arr(self, nums, start, end):
		while start < end:
			nums[start], nums[end] = nums[end], nums[start]
			start += 1
			end -= 1

	def rotate(self, nums: [int], k: int) -> None:
		"""
		Do not return anything, modify nums in-place instead.
		"""
		n = len(nums)
		k %= n
		self.reverse_arr(nums, 0, n-1)
		self.reverse_arr(nums, 0, k-1)
		self.reverse_arr(nums, k, n-1)

nums = [1,2,3,4,5,6,7]
k = 3
print("nums before rotating: {}".format(nums))
obj = Solution()
obj.rotate(nums, k)
print("nums after rotating: {}".format(nums))
