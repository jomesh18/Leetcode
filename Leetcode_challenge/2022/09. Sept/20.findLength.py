'''
718. Maximum Length of Repeated Subarray
Medium

4877

119

Add to List

Share
Given two integer arrays nums1 and nums2, return the maximum length of a subarray that appears in both arrays.

 

Example 1:

Input: nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
Output: 3
Explanation: The repeated subarray with maximum length is [3,2,1].
Example 2:

Input: nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]
Output: 5
 

Constraints:

1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 100
Accepted
209,961
Submissions
408,165
'''
#tle, naive method O(m*n*min(m, n))
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        n2starts = defaultdict(list)
        ans = 0
        for i, x in enumerate(nums2):
            n2starts[x].append(i)
        for i, x in enumerate(nums1):
            for j in n2starts[x]:
                k = 0
                while i+k < m and j+k < n and nums1[i+k] == nums2[j+k]:
                    k += 1
                ans = max(ans, k)
        return ans

#binary search (accepted)
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        lo, hi = 0, (m+n)+1
        
        def check(k):
            seen = set(tuple(nums1[i:i+k]) for i in range(m-k+1))
            return any(tuple(nums2[i:i+k]) in seen for i in range(n-k+1))
        
        while lo < hi:
            mid = (lo+hi)//2
            if check(mid):
                lo = mid + 1
            else:
                hi = mid
        return lo - 1

class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        
        dp = [[0]*(n+1) for _ in range(m+1)]
        ans = 0
        for i in range(1, m+1):
            for j in range(1, n+1):
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                    ans = max(dp[i][j], ans)
        # print(dp)
        return ans
