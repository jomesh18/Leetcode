'''
Intersection of Two Arrays II

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
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_dict = Counter(nums1)
        nums2_dict = Counter(nums2)
        res = []
        for val in nums1_dict:
            if val in nums2_dict:
                res.extend([val]*min(nums1_dict[val], nums2_dict[val]))
        return res

#leetcode fastest
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersection = []
        items = dict()
        for i in nums1:
            items[i] = items.get(i, 0) + 1
        print(items)
        for i in nums2:
            val = items.get(i, None)
            if val != None and val > 0:
                intersection.append(i)
                items[i] -= 1
        return intersection