'''
Combinations

Given two integers n and k, return all possible combinations of k numbers out of the range [1, n].

You may return the answer in any order.

 

Example 1:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

Example 2:

Input: n = 1, k = 1
Output: [[1]]

 

Constraints:

    1 <= n <= 20
    1 <= k <= n

'''
#backtracking solution
# class Solution:
#     def combine(self, n: int, k: int) -> [[int]]:
#         res = []
#         def backtrack(temp):
#             if len(temp) == k:
#                 res.append(temp)
#                 return
#             for num in range(1, n+1):
#                 if not temp or temp and temp[-1]<num:
#                     if temp and temp[0] > n-k+1:
#                         break
#                     backtrack(temp+[num])

#         backtrack([])
#         return res


#iterative, by stafan pochmann

class Solution:
    def combine(self, n, k):
        combs = [[]]
        for _ in range(k):
            combs = [[i] + c for c in combs for i in range(1, c[0] if c else n+1)]
        return combs

n = 4
k = 2
# Output: [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]

# n = 1
# k = 1
# # Output: [[1]]

# n = 3
# k = 2
# # Output = [[1, 2], [1, 3], [2, 3]]

# n = 3
# k = 3
# # Output = [[1, 2], [1, 3], [2, 3]]

n = 4
k = 3
# # Output:[[1, 2, 3], [1, 2, 4], [1, 3, 4], [2, 3, 4]]

sol = Solution()
print(sol.combine(n, k))
                