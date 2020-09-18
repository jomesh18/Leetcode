class Solution:
    def rotate(self, nums: [int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for _ in range(k):
        	nums.insert(0, nums.pop(len(nums)-1))

nums = [1,2,3,4,5,6,7]
k = 3
print("nums before rotating: {}".format(nums))
obj = Solution()
obj.rotate(nums, k)
print("nums after roatating: {}".format(nums))
