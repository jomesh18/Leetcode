class Solution:
    def arrayPairSum(self, nums: [int]) -> int:
        nums.sort()
        sum = 0
        for i in range(0,len(nums),2):
            sum += nums[i]
        return sum

obj = Solution()
nums = [1,4,3,2]
print(obj.arrayPairSum(nums))
nums = [1,2,3,2]
print(obj.arrayPairSum(nums))

# from leetcode
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return(sum(nums[::2]))
