'''
3342. Find Minimum Time to Reach Last Room II
Solved
Medium
Topics
premium lock icon
Companies
Hint
There is a dungeon with n x m rooms arranged as a grid.

You are given a 2D array moveTime of size n x m, where moveTime[i][j] represents the minimum time in seconds when you can start moving to that room. You start from the room (0, 0) at time t = 0 and can move to an adjacent room. Moving between adjacent rooms takes one second for one move and two seconds for the next, alternating between the two.

Return the minimum time to reach the room (n - 1, m - 1).

Two rooms are adjacent if they share a common wall, either horizontally or vertically.

 

Example 1:

Input: moveTime = [[0,4],[4,4]]

Output: 7

Explanation:

The minimum time required is 7 seconds.

At time t == 4, move from room (0, 0) to room (1, 0) in one second.
At time t == 5, move from room (1, 0) to room (1, 1) in two seconds.
Example 2:

Input: moveTime = [[0,0,0,0],[0,0,0,0]]

Output: 6

Explanation:

The minimum time required is 6 seconds.

At time t == 0, move from room (0, 0) to room (1, 0) in one second.
At time t == 1, move from room (1, 0) to room (1, 1) in two seconds.
At time t == 3, move from room (1, 1) to room (1, 2) in one second.
At time t == 4, move from room (1, 2) to room (1, 3) in two seconds.
Example 3:

Input: moveTime = [[0,1],[1,2]]

Output: 4

 

Constraints:

2 <= n == moveTime.length <= 750
2 <= m == moveTime[i].length <= 750
0 <= moveTime[i][j] <= 109
'''
class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        m, n = len(moveTime), len(moveTime[0])
        d = [[float('inf')]*n for _ in range(m)]
        dirs = [(-1, 0), (0, -1), (0, 1), (1, 0)]
        pq = [(0, 0, 0, True)] # t, r, c, moveT
        while pq:
            # print(pq)
            t, i, j, moveT = heappop(pq)
            if i == m-1 and j == n-1: continue
            for di, dj in dirs:
                ni, nj = i+di, j+dj
                if ni < 0 or nj < 0 or ni == m or nj == n:
                    continue
                curr_t = max(t, moveTime[ni][nj]) + (1 if moveT else 2)
                if curr_t < d[ni][nj]:
                    d[ni][nj] = curr_t
                    heappush(pq, (curr_t, ni, nj, not moveT))
        
        return d[-1][-1]
