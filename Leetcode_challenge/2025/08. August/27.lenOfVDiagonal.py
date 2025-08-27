'''
3459. Length of Longest V-Shaped Diagonal Segment
Solved
Hard
Topics
premium lock icon
Companies
Hint
You are given a 2D integer matrix grid of size n x m, where each element is either 0, 1, or 2.

A V-shaped diagonal segment is defined as:

The segment starts with 1.
The subsequent elements follow this infinite sequence: 2, 0, 2, 0, ....
The segment:
Starts along a diagonal direction (top-left to bottom-right, bottom-right to top-left, top-right to bottom-left, or bottom-left to top-right).
Continues the sequence in the same diagonal direction.
Makes at most one clockwise 90-degree turn to another diagonal direction while maintaining the sequence.


Return the length of the longest V-shaped diagonal segment. If no valid segment exists, return 0.

 

Example 1:

Input: grid = [[2,2,1,2,2],[2,0,2,2,0],[2,0,1,1,0],[1,0,2,2,2],[2,0,0,2,2]]

Output: 5

Explanation:



The longest V-shaped diagonal segment has a length of 5 and follows these coordinates: (0,2) → (1,3) → (2,4), takes a 90-degree clockwise turn at (2,4), and continues as (3,3) → (4,2).

Example 2:

Input: grid = [[2,2,2,2,2],[2,0,2,2,0],[2,0,1,1,0],[1,0,2,2,2],[2,0,0,2,2]]

Output: 4

Explanation:



The longest V-shaped diagonal segment has a length of 4 and follows these coordinates: (2,3) → (3,2), takes a 90-degree clockwise turn at (3,2), and continues as (2,1) → (1,0).

Example 3:

Input: grid = [[1,2,2,2,2],[2,2,2,2,0],[2,0,0,0,0],[0,0,2,2,2],[2,0,0,2,0]]

Output: 5

Explanation:



The longest V-shaped diagonal segment has a length of 5 and follows these coordinates: (0,0) → (1,1) → (2,2) → (3,3) → (4,4).

Example 4:

Input: grid = [[1]]

Output: 1

Explanation:

The longest V-shaped diagonal segment has a length of 1 and follows these coordinates: (0,0).

 

Constraints:

n == grid.length
m == grid[i].length
1 <= n, m <= 500
grid[i][j] is either 0, 1 or 2.
'''
class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        # dp = [[[[[-1]*n for _ in range(m)] for _ in range(3)] for _ in range(2)] for _ in range(4)]
        dp = {}
        neighbors = [[-1, 1], [1, 1], [1, -1], [-1, -1]]
        def dfs(i, j, nex, rotated, direction):
            # print(i, j, nex, rotated, direction)
            # if dp[i][j][nex][rotated][direction] != -1:
            #     return dp[i][j][nex][rotated][direction]
            if (i, j, nex, rotated, direction) in dp:
                return dp[(i, j, nex, rotated, direction)]
            di, dj = neighbors[direction]
            ni, nj = i+di, j+dj
            ans = 0
            if check_inside(ni, nj) and grid[ni][nj] == nex:
                ans = max(ans, 1+dfs(ni, nj, 2-nex, rotated, direction))
            if not rotated:
                new_dir = (direction + 1) % 4
                di, dj = neighbors[new_dir]
                ni, nj = i+di, j+dj
                if check_inside(ni, nj) and grid[ni][nj] == nex:
                    curr = 1+dfs(ni, nj, 2-nex, True, new_dir)
                    ans = max(ans, curr)
                    # print('ni', ni, nj, curr, ans)
            # dp[i][j][nex][rotated][direction] = ans
            dp[(i, j, nex, rotated, direction)] = ans
            return ans

        def check_inside(i, j):
            return not(i < 0 or j < 0 or i >= m or j >= n)

        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res = max(res, 1)
                    for k, (di, dj) in enumerate(neighbors):
                        ni, nj = i+di, j+dj
                        if check_inside(ni, nj) and grid[ni][nj] == 2:
                            curr = 2+dfs(ni, nj, 0, False, k)
                            res = max(res, curr)
                            # print(i, j, ni, nj, k, res, curr)

        return res
