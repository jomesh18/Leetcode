'''
719. Find K-th Smallest Pair Distance
Hard

3180

104

Add to List

Share
The distance of a pair of integers a and b is defined as the absolute difference between a and b.

Given an integer array nums and an integer k, return the kth smallest distance among all the pairs nums[i] and nums[j] where 0 <= i < j < nums.length.

 

Example 1:

Input: nums = [1,3,1], k = 1
Output: 0
Explanation: Here are all the pairs:
(1,3) -> 2
(1,1) -> 0
(3,1) -> 2
Then the 1st smallest distance pair is (1,1), and its distance is 0.
Example 2:

Input: nums = [1,1,1], k = 2
Output: 0
Example 3:

Input: nums = [1,6,1], k = 3
Output: 5
 

Constraints:

n == nums.length
2 <= n <= 104
0 <= nums[i] <= 106
1 <= k <= n * (n - 1) / 2
'''
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        
        # sums = []
        # for i in range(n):
        #     for j in range(i+1, n):
        #         sums.append(nums[j] - nums[i])
        # sums.sort()
        
        
        def find_pos(dist):
            count = 0
            for i in range(n-1):
                lo, hi = i+1, n
                while lo < hi:
                    m = (lo + hi) // 2
                    if nums[m] - nums[i] <= dist:
                        lo = m + 1
                    else:
                        hi = m
                count += lo - i - 1
                if count > k: return 1
            return 1 if count > k else (-1 if count < k else 0)
            
        lo, hi = 0, nums[-1]-nums[0]
        ans = hi
        while lo < hi:
            mid = (lo + hi) // 2
            pos = find_pos(mid)
            if pos == 1 or pos == 0:
                ans = mid
                hi = mid
            elif pos == -1:
                lo = mid + 1
        return ans
    