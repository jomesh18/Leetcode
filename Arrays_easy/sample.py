class Solution:
    def findMaxConsecutiveOnes(self, nums: [int]) -> int:
        length = 0
        i = 0
        while i<len(nums):
            if nums[i] == 1:
                count = 0
                j = i
                while j<len(nums) and nums[j] == 1:
                    count += 1
                    j += 1
                if count > length:
                    length = count
                i = j
            i += 1
        return length

obj = Solution()
nums = [1,1,0,1,1,1]
print(nums)
print(obj.findMaxConsecutiveOnes(nums))
