'''
2179. Count Good Triplets in an Array
Solved
Hard
Topics
premium lock icon
Companies
Hint
You are given two 0-indexed arrays nums1 and nums2 of length n, both of which are permutations of [0, 1, ..., n - 1].

A good triplet is a set of 3 distinct values which are present in increasing order by position both in nums1 and nums2. In other words, if we consider pos1v as the index of the value v in nums1 and pos2v as the index of the value v in nums2, then a good triplet will be a set (x, y, z) where 0 <= x, y, z <= n - 1, such that pos1x < pos1y < pos1z and pos2x < pos2y < pos2z.

Return the total number of good triplets.

 

Example 1:

Input: nums1 = [2,0,1,3], nums2 = [0,1,2,3]
Output: 1
Explanation: 
There are 4 triplets (x,y,z) such that pos1x < pos1y < pos1z. They are (2,0,1), (2,0,3), (2,1,3), and (0,1,3). 
Out of those triplets, only the triplet (0,1,3) satisfies pos2x < pos2y < pos2z. Hence, there is only 1 good triplet.
Example 2:

Input: nums1 = [4,0,1,3,2], nums2 = [4,1,0,2,3]
Output: 4
Explanation: The 4 good triplets are (4,0,3), (4,0,2), (4,1,3), and (4,1,2).
 

Constraints:

n == nums1.length == nums2.length
3 <= n <= 105
0 <= nums1[i], nums2[i] <= n - 1
nums1 and nums2 are permutations of [0, 1, ..., n - 1].
'''
class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        left = [0]*n
        right = [0]*n

        pos2 = [0]*n
        for i, b in enumerate(nums2):
            pos2[b] = i
        
        pos2_arr = SortedList([pos2[nums1[0]]])
        for i in range(1, n):
            pos2_arr.add(pos2[nums1[i]])
            j = bisect_left(pos2_arr, pos2[nums1[i]])
            left[i] = j

        pos2_arr = SortedList([pos2[nums1[-1]]])
        right[-1] = 0
        for i in range(n-2, -1, -1):
            j = bisect_left(pos2_arr, pos2[nums1[i]])
            right[i] = len(pos2_arr)-j
            pos2_arr.add(pos2[nums1[i]])
        
        ans = 0
        for i in range(1, n-1):
            ans += left[i]*right[i]
        return ans
