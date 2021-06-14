'''
Intersection of Two Arrays

Solution
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

 

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.
 

Constraints:

1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000
'''

# class Solution:
#     def intersection(self, nums1: [int], nums2: [int]) -> [int]:
#       return list(set(nums1).intersection(set(nums2)))

# class Solution:
#     def intersection(self, nums1: [int], nums2: [int]) -> [int]:
#         res = set()
#         nums1, nums2 = set(nums1), set(nums2)
#         for num in nums1:
#             if num in nums2:
#                 res.add(num)
#         return list(res)

#O(nlogn) time, O(1) space
class Solution:
    def intersection(self, nums1: [int], nums2: [int]) -> [int]:
        nums1.sort()
        nums2.sort()
        i, j, res = 0, 0, []
        while i<len(nums1) and j<len(nums2):
            if nums1[i] == nums2[j]:
                if not res or res and res[-1]!= nums1[i]:
                    res.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i]>nums2[j]:
                j += 1
            else:
                i += 1
        return res

nums1 = [1,2,2,1]
nums2 = [2,2]
# Output: [2]

# nums1 = [4,9,5]
# nums2 = [9,4,9,8,4]
# # Output: [9,4]

s = Solution()
print(s.intersection(nums1, nums2))
