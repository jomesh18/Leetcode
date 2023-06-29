'''
864. Shortest Path to Get All Keys
Hard

1312

57

Add to List

Share
You are given an m x n grid grid where:

'.' is an empty cell.
'#' is a wall.
'@' is the starting point.
Lowercase letters represent keys.
Uppercase letters represent locks.
You start at the starting point and one move consists of walking one space in one of the four cardinal directions. You cannot walk outside the grid, or walk into a wall.

If you walk over a key, you can pick it up and you cannot walk over a lock unless you have its corresponding key.

For some 1 <= k <= 6, there is exactly one lowercase and one uppercase letter of the first k letters of the English alphabet in the grid. This means that there is exactly one key for each lock, and one lock for each key; and also that the letters used to represent the keys and locks were chosen in the same order as the English alphabet.

Return the lowest number of moves to acquire all keys. If it is impossible, return -1.

 

Example 1:


Input: grid = ["@.a..","###.#","b.A.B"]
Output: 8
Explanation: Note that the goal is to obtain all the keys not to open all the locks.
Example 2:


Input: grid = ["@..aA","..B#.","....b"]
Output: 6
Example 3:


Input: grid = ["@Aa"]
Output: -1
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 30
grid[i][j] is either an English letter, '.', '#', or '@'.
The number of keys in the grid is in the range [1, 6].
Each key in the grid is unique.
Each key in the grid has a matching lock.
'''
class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        grid = [list(r) for r in grid]
        m, n = len(grid), len(grid[0])
        tot_k = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '@':
                    start = (i, j)
                    grid[i][j] = '.'
                elif grid[i][j] == '.' or grid[i][j] == '#':
                    continue
                elif grid[i][j].islower():
                    tot_k += 1
        mask = 0
        all_collected = (1<<tot_k)-1
        q = [(mask, start[0], start[1])]
        dp = dict()
        dp[(mask, start[0], start[1])] = 0
        while q:
            nq = []
            # print("q = {}".format(q))
            for mask, i, j in q:
                moves = dp[(mask, i, j)]
                for ni, nj in [(i-1, j), (i, j-1), (i, j+1), (i+1, j)]:
                    if 0<=ni<m and 0<=nj<n and grid[ni][nj] != '#':
                        key = (mask, ni, nj)
                        if grid[ni][nj] == '.':
                            if dp.get(key, float('inf')) > moves+1:
                                dp[key] = moves + 1
                                nq.append(key)
                        elif grid[ni][nj].isupper():
                            if mask & (1<<(ord(grid[ni][nj].lower())-ord('a'))):
                                if dp.get(key, float('inf')) > moves+1:
                                    dp[key] = moves + 1
                                    nq.append(key)
                        elif grid[ni][nj].islower():
                            new_mask = mask | (1<<ord(grid[ni][nj].lower())-ord('a'))
                            if new_mask == all_collected: return dp[(mask, i, j)] + 1
                            key = (new_mask,ni,nj)
                            if dp.get(key, float('inf')) > moves+1:
                                dp[key] = moves + 1
                                nq.append(key)
            # print(dp)
            q = nq
        return -1
