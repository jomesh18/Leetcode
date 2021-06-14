'''
Intersection of Two Arrays II

Solution
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

 

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.
 

Constraints:

1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000
 

Follow up:

What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
'''

# O(nlogn) time O(max(N, M)) if already sorted, O(1) space
# class Solution:
#     def intersect(self, nums1: [int], nums2: [int]) -> [int]:
#         nums1.sort()
#         nums2.sort()
#         i, j, res = 0, 0, []
#         while i<len(nums1) and j<len(nums2):
#             if nums1[i] == nums2[j]:
#                 res.append(nums1[i])
#                 i += 1
#                 j += 1
#             elif nums1[i] > nums2[j]:
#                 j += 1
#             else:
#                 i += 1
#         return res

# #O(n+m) (O(n) to iterate nums1, O(m) to iterate nums2) time, O(n) space
# class Solution:
#     def intersect(self, nums1: [int], nums2: [int]) -> [int]:
#         nums1_dict = {}
#         res = []
#         for num in nums1:
#             if num not in nums1_dict: # use nums1_dict.get(num, 0)
#                 nums1_dict[num] = 1
#             else:
#                 nums1_dict[num] += 1
#         for num in nums2:
#             if num in nums1_dict and nums1_dict[num] > 0:
#                 res.append(num) # or res += num, another form which is faster
#                 nums1_dict[num] -= 1
#         return res

'''
What if nums1's size is small compared to nums2's size? Which algorithm is better?
This one is a bit tricky. Let's say nums1 is K size. Then we should do binary search for every element in nums1. Each lookup is O(log N), and if we do K times, we have O(K log N).
If K this is small enough, O(K log N) < O(max(N, M)). Otherwise, we have to use the previous two pointers method.
let's say A = [1, 2, 2, 2, 2, 2, 2, 2, 1], B = [2, 2]. For each element in B, we start a binary search in A. To deal with duplicate entry, once you find an entry, all the duplicate element is around that that index, so you can do linear search scan afterward.

Time complexity, O(K(logN) + N). Plus N is worst case scenario which you have to linear scan every element in A. But on average, that shouldn't be the case. so I'd say the Time complexity is O(K(logN) + c), c (constant) is number of linear scan you did.

What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
This one is open-ended. But Map-Reduce I believe is a good answer.
'''

#using counter
from collections import Counter
class Solution(object):
    def intersect(self, nums1, nums2):

        counts = Counter(nums1)
        res = []

        for num in nums2:
            if counts[num] > 0:
                res += num,
                counts[num] -= 1

        return res


nums1 = [1,2,2,1]
nums2 = [2,2]
# Output: [2,2]
# nums1 = [4,9,5]
# nums2 = [9,4,9,8,4]
# Output: [4,9]

s = Solution()
print(s.intersect(nums1, nums2))
