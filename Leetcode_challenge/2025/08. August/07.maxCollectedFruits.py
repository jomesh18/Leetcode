'''
3363. Find the Maximum Number of Fruits Collected
Solved
Hard
Topics
premium lock icon
Companies
Hint
There is a game dungeon comprised of n x n rooms arranged in a grid.

You are given a 2D array fruits of size n x n, where fruits[i][j] represents the number of fruits in the room (i, j). Three children will play in the game dungeon, with initial positions at the corner rooms (0, 0), (0, n - 1), and (n - 1, 0).

The children will make exactly n - 1 moves according to the following rules to reach the room (n - 1, n - 1):

The child starting from (0, 0) must move from their current room (i, j) to one of the rooms (i + 1, j + 1), (i + 1, j), and (i, j + 1) if the target room exists.
The child starting from (0, n - 1) must move from their current room (i, j) to one of the rooms (i + 1, j - 1), (i + 1, j), and (i + 1, j + 1) if the target room exists.
The child starting from (n - 1, 0) must move from their current room (i, j) to one of the rooms (i - 1, j + 1), (i, j + 1), and (i + 1, j + 1) if the target room exists.
When a child enters a room, they will collect all the fruits there. If two or more children enter the same room, only one child will collect the fruits, and the room will be emptied after they leave.

Return the maximum number of fruits the children can collect from the dungeon.

 

Example 1:

Input: fruits = [[1,2,3,4],[5,6,8,7],[9,10,11,12],[13,14,15,16]]

Output: 100

Explanation:



In this example:

The 1st child (green) moves on the path (0,0) -> (1,1) -> (2,2) -> (3, 3).
The 2nd child (red) moves on the path (0,3) -> (1,2) -> (2,3) -> (3, 3).
The 3rd child (blue) moves on the path (3,0) -> (3,1) -> (3,2) -> (3, 3).
In total they collect 1 + 6 + 11 + 16 + 4 + 8 + 12 + 13 + 14 + 15 = 100 fruits.

Example 2:

Input: fruits = [[1,1],[1,1]]

Output: 4

Explanation:

In this example:

The 1st child moves on the path (0,0) -> (1,1).
The 2nd child moves on the path (0,1) -> (1,1).
The 3rd child moves on the path (1,0) -> (1,1).
In total they collect 1 + 1 + 1 + 1 = 4 fruits.

 

Constraints:

2 <= n == fruits.length == fruits[i].length <= 1000
0 <= fruits[i][j] <= 1000
'''
class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        ans = 0
        m, n = len(fruits), len(fruits[0])
        for i in range(n):
            ans += fruits[i][i]
            fruits[i][i] = 0
            i += 1
        half = n // 2
        dp = [[0]*n for _ in range(n)]
        dp[0][n-1] = fruits[0][n-1]
        for i in range(1, n-1):
            if i < half:
                for j in range(n-1-i, n, 1):
                    dp[i][j] = fruits[i][j]
                    curr_max = 0 
                    if j >= n-1-i+2:
                        curr_max = max(curr_max, dp[i-1][j-1])  
                    if j != n-1-i:
                        curr_max = max(curr_max, dp[i-1][j])
                    if j+1 < n:
                        curr_max = max(curr_max, dp[i-1][j+1])
                    dp[i][j] += curr_max
            else:
                for j in range(i+1, n):
                    dp[i][j] = fruits[i][j]
                    curr_max = max(dp[i-1][j-1], dp[i-1][j])
                    if j+1 < n:
                        curr_max = max(curr_max, dp[i-1][j+1])
                    dp[i][j] += curr_max
        
        # print(dp)
        ans += dp[n-2][-1]

        dp = [[0]*n for _ in range(n)]
        dp[n-1][0] = fruits[n-1][0]
        for j in range(1, n):
            if j < half:
                first = n-1-j
                for i in range(first, n):
                    dp[i][j] = fruits[i][j]
                    curr_max = 0
                    if i >= first+2:
                        curr_max = max(curr_max, dp[i-1][j-1])
                    if i > first:
                        curr_max = max(curr_max, dp[i][j-1])
                    if i+1 < n:
                        curr_max = max(curr_max, dp[i+1][j-1])
                    dp[i][j] += curr_max
            else:
                
                first = j+1
                for i in range(first, n):
                    dp[i][j] = fruits[i][j]
                    curr_max = max(dp[i-1][j-1], dp[i][j-1])
                    if i+1 < n:
                        curr_max = max(curr_max, dp[i+1][j-1])
                    dp[i][j] += curr_max
        # print(dp)
        ans += dp[-1][-2]
        return ans
