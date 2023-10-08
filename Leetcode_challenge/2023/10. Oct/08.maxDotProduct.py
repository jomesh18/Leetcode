class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        max1, min1, max2, min2 = max(nums1), min(nums1), max(nums2), min(nums2)
        if max1 < 0 and min2 > 0:
            return max1*min2
        if max2 < 0 and min1 > 0:
            return max2*min1
        memo = {}
        def dp(i, j):
            if i == len(nums1) or j == len(nums2):
                return 0
            if (i, j) in memo: return memo[(i, j)]
            ans = nums1[i]*nums2[j] + dp(i+1, j+1)
            ans = max(ans, dp(i+1, j), dp(i, j+1))
            memo[(i, j)] = ans
            return ans
        return dp(0, 0)