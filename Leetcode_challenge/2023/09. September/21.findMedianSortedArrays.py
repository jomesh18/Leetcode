'''
4. Median of Two Sorted Arrays
Hard

25831

2843

Add to List

Share
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
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        m, n = len(nums1), len(nums2)
        lo, hi = 0, m
        while lo <= hi:
            mid1 = (lo+hi)//2
            mid2 = (m+n+1)//2 - mid1
            l1 = nums1[mid1-1] if mid1 != 0 else float('-inf')
            l2 = nums2[mid2-1] if mid2 != 0 else float('-inf')
            r1 = nums1[mid1] if mid1 != m else float('inf')
            r2 = nums2[mid2] if mid2 != n else float('inf')
            
            if l1 <= r2 and l2 <= r1:
                if (m+n) & 1:
                    return max(l1, l2)
                else:
                    return (max(l1,l2) + min(r1, r2))/2
            elif l1 > r2:
                hi = mid1-1
            else:
                lo = mid1+1
                