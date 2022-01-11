'''
Sort Array By Parity II

Given an array of integers nums, half of the integers in nums are odd, and the other half are even.

Sort the array so that whenever nums[i] is odd, i is odd, and whenever nums[i] is even, i is even.

Return any answer array that satisfies this condition.

 

Example 1:

Input: nums = [4,2,5,7]
Output: [4,5,2,7]
Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.

Example 2:

Input: nums = [2,3]
Output: [2,3]

 

Constraints:

    2 <= nums.length <= 2 * 104
    nums.length is even.
    Half of the integers in nums are even.
    0 <= nums[i] <= 1000

 

Follow Up: Could you solve it in-place?
'''
# class Solution:
#     def sortArrayByParityII(self, nums: [int]) -> [int]:
#         for i in range(len(nums)):
#             index_status, num_status = (i%2), (nums[i]%2)
#             if (index_status and num_status) or (not index_status and not num_status):
#                 continue
#             else:
#                 for j in range(len(nums)-1, -1, -1):
#                     if (nums[j] % 2) == index_status:
#                         nums[j], nums[i] = nums[i], nums[j]
#                         break
#         return nums

#from leetcode
# class Solution:
#     def sortArrayByParityII(self, nums: [int]) -> [int]:
#             e = 0 #even_index
#             o = 1 #odd_index
        
#             while e<len(nums) and o<len(nums):
#                 if nums[e]%2==0:
#                     e+=2
#                 else:
#                     if nums[o]%2!=0:
#                         o+=2
#                     else:
#                         nums[e],nums[o] = nums[o],nums[e]
#                         e+=2
#                         o+=2
#             return nums

#from leetcode, solution
class Solution:
    def sortArrayByParityII(self, A):
        j = 1
        for i in range(0, len(A), 2):
            if A[i] % 2:
                while A[j] % 2:
                    j += 2
                A[i], A[j] = A[j], A[i]
        return A

nums = [4,2,5,7]
# # Output: [4,5,2,7]

nums = [2,3]
# # Output: [2,3]

nums = [4,1,1,0,1,0]
# Output: [4,1,0,1,0,1]

sol = Solution()
print(sol.sortArrayByParityII(nums))
