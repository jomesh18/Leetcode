'''
K Inverse Pairs Array
For an integer array nums, an inbverse pair is a pair of integers [i, j] where 0 <= i < j < nums.length and nums[i] > nums[j].

Given two integers n and k, return the number of different arrays consist of numbers from 1 to n such that there are exactly k inverse pairs. Since the answer can be huge, return it modulo 109 + 7.

 

Example 1:

Input: n = 3, k = 0
Output: 1
Explanation: Only the array [1,2,3] which consists of numbers from 1 to 3 has exactly 0 inverse pairs.
Example 2:

Input: n = 3, k = 1
Output: 2
Explanation: The array [1,3,2] and [2,1,3] have exactly 1 inverse pair.
 

Constraints:

1 <= n <= 1000
0 <= k <= 1000
'''
#naive solution
# class Solution:
#     def kInversePairs(self, n: int, k: int) -> int:
#         nums = [i for i in range(1, n+1)]
#         combs = self.combinations(nums)
#         res, count = {}, 0
#         for num in combs:
#         	temp = self.check_k_inverse(num)
#         	if temp in res:
#         		res[temp].append(num)
#         	else:
#         		res[temp] = [num]
#         for key in res:
#         	print("{}".format(key))
#         	print(res[key])

#     def combinations(self, nums):
#     	res = []
#     	def helper(nums, i):
#     		if i == len(nums):
#     			res.append(nums[:])
#     		for j in range(i, len(nums)):
#     			nums[i], nums[j] = nums[j], nums[i]
#     			helper(nums, i+1)
#     			nums[i], nums[j] = nums[j], nums[i]
#     	helper(nums, 0)
#     	return res

#     def check_k_inverse(self, nums):
#     	count = 0
#     	for i in range(len(nums)):
#     		for j in range(len(nums)):
#     			if i<j and nums[i]>nums[j]:
#     				count += 1
#     	return count

#from leetcode
class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        dp = [[1] * (k+1) for _ in range(n+1)]
        sp = [[1] * (k+1) for _ in range(n+1)]
        for i in range(1, n+1):
            for j in range(1, k+1):
                dp[i][j] = sp[i-1][j] if j < i else (sp[i-1][j] - sp[i-1][j-i]) % (10**9 + 7)
                sp[i][j] = (sp[i][j-1] + dp[i][j]) % (10**9 + 7)
        return dp[-1][-1]

n = 4
k = 0
# Output = 1

# n = 3
# k = 1
# # Output: 2

s = Solution()
print(s.kInversePairs(n, k))
