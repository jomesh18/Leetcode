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
Example 3:

Input: nums1 = [0,0], nums2 = [0,0]
Output: 0.00000
Example 4:

Input: nums1 = [], nums2 = [1]
Output: 1.00000
Example 5:

Input: nums1 = [2], nums2 = []
Output: 2.00000
 

Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106
'''
#from leetcode, thushar video, O(log(min(m ,n)))
class Solution:
    def findMedianSortedArrays(self, nums1: [int], nums2: [int]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        len1 = len(nums1)
        len2 = len(nums2)
        l, r = 0, len(nums1)
        print(nums1, nums2)
        while l<=r:
            mid1 = (l+r)//2
            mid2 = (len1+len2+1)//2 - mid1
            # print(mid1, mid2)
            max1left = float("-inf") if mid1==0 else nums1[mid1-1]
            max2left = float("-inf") if mid2==0 else nums2[mid2-1]
            min1right = float("inf") if mid1==len1 else nums1[mid1]
            min2right = float("inf") if mid2==len2 else nums2[mid2]
            if max1left <= min2right and max2left <= min1right:
                if (len1+len2)%2 == 0:
                    return (max(max1left, max2left)+min(min1right, min2right))/2
                else:
                    return max(max1left, max2left)
            elif max1left > min2right:
                r = mid1-1
            else:
                l = mid1+1

nums1 = [1,3]
nums2 = [2]
# Output: 2.00000

nums1 = [1,2]
nums2 = [3,4]
# # # Output: 2.50000

nums1 = [0,0]
nums2 = [0,0]
# # Output: 0.00000

nums1 = []
nums2 = [1]
# # Output: 1.00000

nums1 = [2]
nums2 = []
# # Output: 2.00000

s = Solution()
print(s.findMedianSortedArrays(nums1, nums2))
