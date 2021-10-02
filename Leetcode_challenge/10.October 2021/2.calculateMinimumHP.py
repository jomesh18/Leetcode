'''
174. Dungeon Game

The demons had captured the princess and imprisoned her in the bottom-right corner of a dungeon. The dungeon consists of m x n rooms laid out in a 2D grid. Our valiant knight was initially positioned in the top-left room and must fight his way through dungeon to rescue the princess.

The knight has an initial health point represented by a positive integer. If at any point his health point drops to 0 or below, he dies immediately.

Some of the rooms are guarded by demons (represented by negative integers), so the knight loses health upon entering these rooms; other rooms are either empty (represented as 0) or contain magic orbs that increase the knight's health (represented by positive integers).

To reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.

Return the knight's minimum initial health so that he can rescue the princess.

Note that any room can contain threats or power-ups, even the first room the knight enters and the bottom-right room where the princess is imprisoned.

 

Example 1:


Input: dungeon = [[-2,-3,3],[-5,-10,1],[10,30,-5]]
Output: 7
Explanation: The initial health of the knight must be at least 7 if he follows the optimal path: RIGHT-> RIGHT -> DOWN -> DOWN.
Example 2:

Input: dungeon = [[0]]
Output: 1
 

Constraints:

m == dungeon.length
n == dungeon[i].length
1 <= m, n <= 200
-1000 <= dungeon[i][j] <= 1000
'''
#recursive, tle
# class Solution:
#     def calculateMinimumHP(self, dungeon: [[int]]) -> int:
#         m, n = len(dungeon), len(dungeon[0])

#         def getVal(i, j):
#             if i == m or j == n:
#                 return float("inf")
#             if i == m-1 and j == n-1:
#                 return (1 if dungeon[m-1][n-1] > 0 else -dungeon[m-1][n-1]+1)
#             goRight = getVal(i, j+1)
#             goDown = getVal(i+1, j)
#             minHealthRequired = min(goDown, goRight) - dungeon[i][j]

#             return (1 if minHealthRequired <= 0 else minHealthRequired)
#         return getVal(0, 0)

#recursive, top down
# class Solution:
#     def calculateMinimumHP(self, dungeon: [[int]]) -> int:
#         m, n = len(dungeon), len(dungeon[0])
#         dp = [[None for _ in range(n)] for _ in range(m)]
#         def getVal(i, j):
#             if i == m or j == n:
#                 return float("inf")
#             if dp[i][j]: return dp[i][j]
#             if i == m-1 and j == n-1:
#                 return (1 if dungeon[m-1][n-1] > 0 else -dungeon[m-1][n-1]+1)
#             goRight = getVal(i, j+1)
#             goDown = getVal(i+1, j)
#             minHealthRequired = min(goDown, goRight) - dungeon[i][j]
#             dp[i][j] = 1 if minHealthRequired <= 0 else minHealthRequired
#             return dp[i][j]
#         return getVal(0, 0)


# Bottom up
class Solution:
    def calculateMinimumHP(self, dungeon: [[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])
        dp = [[float("inf") for _ in range(n+1)] for _ in range(m+1)]
        dp[m-1][n], dp[m][n-1] = 1, 1
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                needed = min(dp[i][j+1], dp[i+1][j]) - dungeon[i][j]
                dp[i][j] = needed if needed > 0 else 1
        return dp[0][0]

dungeon = [[-2,-3,3],[-5,-10,1],[10,30,-5]]
# Output: 7

# dungeon = [[0]]
# # Output: 1

sol = Solution()
print(sol.calculateMinimumHP(dungeon))
