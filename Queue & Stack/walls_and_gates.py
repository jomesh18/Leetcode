'''
Walls and Gate

Description
You are given a m x n 2D grid initialized with these three possible values.

-1 - A wall or an obstacle. 0 - A gate. INF - Infinity means an empty room. We use the value 2^31 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647. Fill each empty room with the distance to its nearest gate. If it is impossible to reach a Gate, that room should remain filled with INF

Example
Example1

Input:
[[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
Output:
[[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]

Explanation:
the 2D grid is:
INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
  0  -1 INF INF
the answer is:
  3  -1   0   1
  2   2   1  -1
  1  -1   2  -1
  0  -1   3   4

Example2

Input:
[[0,-1],[2147483647,2147483647]]
Output:
[[0,-1],[1,2]]

'''

from collections import deque
class Solution:
    """
    @param rooms: m x n 2D grid
    @return: nothing
    """
    def wallsAndGates(self, rooms):
        # write your code here
        row = len(rooms)
        column = len(rooms[0])

        def bfs(i, j):
            q = deque([(i, j)])
            count = 0
            visited = set()
            neighbors = [(-1, 0), (0, -1), (0, 1), (1, 0)]
            while q:
                l = len(q)
                for _ in range(l):
                    i, j = q.popleft()
                    if (i, j) not in visited:
                        visited.add((i,j))
                        if rooms[i][j] == 0: return count
                        if i >= 0 and i < row and j >=0 and j< column:
                            q.extend([(i+a, j+b) for a, b in neighbors if i+a >=0 and i+a<row and j+b>=0 and j+b < column and rooms[i+a][j+b]!=-1])
                count += 1
            return 2147483647

        for i in range(row):
            for j in range(column):
                if rooms[i][j] == 2147483647:
                    rooms[i][j] = bfs(i, j)
        return rooms


rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
# Output: [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]
rooms = [[0,-1],[2147483647,2147483647]]
# Output: [[0,-1],[1,2]]
s = Solution()
print(s.wallsAndGates(rooms))
