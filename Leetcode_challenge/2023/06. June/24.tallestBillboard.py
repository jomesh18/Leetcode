'''
956. Tallest Billboard
Hard

1273

41

Add to List

Share
You are installing a billboard and want it to have the largest height. The billboard will have two steel supports, one on each side. Each steel support must be an equal height.

You are given a collection of rods that can be welded together. For example, if you have rods of lengths 1, 2, and 3, you can weld them together to make a support of length 6.

Return the largest possible height of your billboard installation. If you cannot support the billboard, return 0.

 

Example 1:

Input: rods = [1,2,3,6]
Output: 6
Explanation: We have two disjoint subsets {1,2,3} and {6}, which have the same sum = 6.
Example 2:

Input: rods = [1,2,3,4,5,6]
Output: 10
Explanation: We have two disjoint subsets {2,3,5} and {4,6}, which have the same sum = 10.
Example 3:

Input: rods = [1,2]
Output: 0
Explanation: The billboard cannot be supported, so we return 0.
 

Constraints:

1 <= rods.length <= 20
1 <= rods[i] <= 1000
sum(rods[i]) <= 5000
'''
#tle 
# class Solution:
#     def tallestBillboard(self, rods: List[int]) -> int:
#         memo = {}
#         half_sum = sum(rods)//2
#         def helper(i, s1, s2):
#             if s1 > half_sum or s2 > half_sum: return 0
#             if i == len(rods):
#                 if s1 == s2:
#                     return s1
#                 else:
#                     return 0
#             if (i, s1, s2) in memo: return memo[(i, s1, s2)]
#             ans = helper(i+1, s1+rods[i], s2)
#             ans = max(ans, helper(i+1, s1, s2+rods[i]))
#             ans = max(ans, helper(i+1, s1, s2))
#             memo[(i, s1, s2)] = ans
#             return ans
#         return helper(0, 0, 0)

# O(3**(n/2))
class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        n = len(rods)
        
        def helper(half_rod):
            r_set = {(0, 0)}
            for rod in half_rod:
                new_set = set()
                for l, r in r_set:
                    new_set.add((l+rod, r))
                    new_set.add((l, r+rod))
                r_set |= new_set
            dp = {}
            for l, r in r_set:
                dp[l-r] = max(dp.get(l-r, 0), l)
            return dp
            
        first_half = helper(rods[:n//2])
        second_half = helper(rods[n//2:])
        
        ans = 0
        for diff in first_half:
            if -diff in second_half:
                ans = max(ans, first_half[diff] + second_half[-diff])
        return ans

#O(n*m) where m is the max sum of rods
class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        dp = {0: 0}
        for r in rods:
            new_dp = dp.copy()
            for diff, taller in dp.items():
                new_dp[diff+r] = max(new_dp.get(diff+r, 0), taller+r)
                new_dp[abs(r-diff)] = max(new_dp.get(abs(r-diff), 0), max(taller-diff+r, taller))
            dp = new_dp
        return dp[0]


class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        # dp[taller - shorter] = taller
        dp = {0:0}
        
        for r in rods:
            # dp.copy() means we don't add r to these stands.
            new_dp = dp.copy()
            for diff, taller in dp.items():
                shorter = taller - diff
                
                # Add r to the taller stand, thus the height difference is increased to diff + r.
                new_dp[diff + r] = max(new_dp.get(diff + r, 0), taller + r)
                
                # Add r to the shorter stand, the height difference is expressed as abs(shorter + r - taller).
                new_diff = abs(shorter + r - taller)
                new_taller = max(shorter + r, taller)
                new_dp[new_diff] = max(new_dp.get(new_diff, 0), new_taller)
                
            dp = new_dp
            
        # Return the maximum height with 0 difference.
        return dp.get(0, 0)