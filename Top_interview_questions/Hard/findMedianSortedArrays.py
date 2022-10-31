'''
Median of Two Sorted Arrays
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 

Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106
'''
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        if m > n: return self.findMedianSortedArrays(nums2, nums1)
        lo, hi = 0, 2*m+1
        while lo < hi:
            mid1 = (lo+hi)//2
            mid2 = m+n-mid1
            left1 = nums1[(mid1-1)//2] if mid1 > 0 else float('-inf')
            left2 = nums2[(mid2-1)//2] if mid2 > 0 else float('-inf')
            right1 = nums1[mid1//2] if mid1 < 2*m else float('inf')
            right2 = nums2[mid2//2] if mid2 < 2*n else float('inf')
            if left1 > right2:
                hi = mid1
            elif left2 > right1:
                lo = mid1 + 1
            else:
                return (max(left1, left2) + min(right1, right2))/2
        return -1