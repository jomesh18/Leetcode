'''
514 · Paint Fence
Algorithms
Easy
Accepted Rate
40%

DescriptionSolutionNotesDiscussLeaderboard
Description
There is a fence with n posts, each post can be painted with one of the k colors.
You have to paint all the posts such that no more than two adjacent fence posts have the same color.
Return the total number of ways you can paint the fence.

Wechat reply the 【514】 get the latest frequent Interview questions . (wechat id : jiuzhang15)

n and k are non-negative integers.

Example
Example 1:

Input: n=3, k=2  
Output: 6
Explanation:
          post 1,   post 2, post 3
    way1    0         0       1 
    way2    0         1       0
    way3    0         1       1
    way4    1         0       0
    way5    1         0       1
    way6    1         1       0
Example 2:

Input: n=2, k=2  
Output: 4
Explanation:
          post 1,   post 2
    way1    0         0       
    way2    0         1            
    way3    1         0          
    way4    1         1       
    '''

#dp
# class Solution:
#     """
#     @param n: non-negative integer, n posts
#     @param k: non-negative integer, k colors
#     @return: an integer, the total number of ways
#     """
#     def numWays(self, n, k):
#         # write your code here
#         if k <= 1 and n > k*2: return 0
#         if n == 1: return k
#         dp = [[0]*(n+1) for _ in range(3)]
#         dp[0][2] = k
#         dp[1][2] = k*(k-1)
#         dp[2][2] = dp[0][2]+dp[1][2]
#         for i in range(3, n+1):
#             dp[0][i] = dp[1][i-1]
#             dp[1][i] = dp[2][i-1]*(k-1)
#             dp[2][i] = dp[0][i]+dp[1][i]
#         # print(dp)
#         return dp[2][n]

#memo
class Solution:
    """
    @param n: non-negative integer, n posts
    @param k: non-negative integer, k colors
    @return: an integer, the total number of ways
    """
    def numWays(self, n, k):
        # write your code here
        if k <= 1 and n > k*2: return 0
        if n == 1: return k
        if n == 2: return k*k
        dp = [[0]*(n+1) for _ in range(3)]
        def helper(i, status):
            if i == 2 and status == 0 : return k
            if i == 2 and status == 1 : return k*(k-1)
            if i == 2 and status == 2 : return k*k
            if dp[status][i] != 0: return dp[status][i]
            dp[0][i] = helper(i-1, 1)
            dp[1][i] = helper(i-1, 2) * (k-1)
            dp[2][i] = dp[0][i] + dp[1][i]

            return dp[status][i]
        return helper(n, 2)

n=3
k=2  
# Output: 6

n=2
k=2  
# # Output: 4

n = 1
k = 1
# # Output: 1

n = 10
k = 3
# # Output: 27408

sol = Solution()
print(sol.numWays(n, k))
