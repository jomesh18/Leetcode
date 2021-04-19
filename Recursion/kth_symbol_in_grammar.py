'''
K-th Symbol in Grammar

On the first row, we write a 0. Now in every subsequent row, we look at the previous row and replace each occurrence of 0 with 01, and each occurrence of 1 with 10.

Given row N and index K, return the K-th indexed symbol in row N. (The values of K are 1-indexed.) (1 indexed).

Examples:
Input: N = 1, K = 1
Output: 0

Input: N = 2, K = 1
Output: 0

Input: N = 2, K = 2
Output: 1

Input: N = 4, K = 5
Output: 1

Explanation:
row 1: 0
row 2: 01
row 3: 0110
row 4: 01101001

Note:

    N will be an integer in the range [1, 30].
    K will be an integer in the range [1, 2^(N-1)].

'''
#naive way, timelimit exceeded
# class Solution:
#     def kthGrammar(self, N: int, K: int) -> int:
#         def helper(res):
#             if not res: return res
#             return '01'+helper(res[1:]) if res[0] == '0' else '10'+helper(res[1:])

#         res = '0'
#         for _ in range(N-1):
#             ans = helper(res)
#             print(ans)
#             res = ans
#         return res[K-1]

class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        def helper(N, K):
            if N==0 and K==0:
                return '0'
            ans = helper(N-1, K//2)
            ans = '01' if ans == '0' else '10'
            return ans[1] if K%2 else ans[0]
        return helper(N-1, K-1)

#from leetcode
class Solution:
    def kthGrammar(self, N, K):
        return bin(K - 1).count('1') & 1
        
# N = 1
# K = 1
# Output: 0

# N = 2
# K = 1
# Output: 0

# N = 2
# K = 2
# Output: 1

# N = 4
# K = 5
# Output: 1

N = 30
K = 434991989
s = Solution()
print(s.kthGrammar(N, K))
