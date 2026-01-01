'''
1970. Last Day Where You Can Still Cross
Solved
Hard
Topics
premium lock icon
Companies
Hint
There is a 1-based binary matrix where 0 represents land and 1 represents water. You are given integers row and col representing the number of rows and columns in the matrix, respectively.

Initially on day 0, the entire matrix is land. However, each day a new cell becomes flooded with water. You are given a 1-based 2D array cells, where cells[i] = [ri, ci] represents that on the ith day, the cell on the rith row and cith column (1-based coordinates) will be covered with water (i.e., changed to 1).

You want to find the last day that it is possible to walk from the top to the bottom by only walking on land cells. You can start from any cell in the top row and end at any cell in the bottom row. You can only travel in the four cardinal directions (left, right, up, and down).

Return the last day where it is possible to walk from the top to the bottom by only walking on land cells.

 

Example 1:


Input: row = 2, col = 2, cells = [[1,1],[2,1],[1,2],[2,2]]
Output: 2
Explanation: The above image depicts how the matrix changes each day starting from day 0.
The last day where it is possible to cross from top to bottom is on day 2.
Example 2:


Input: row = 2, col = 2, cells = [[1,1],[1,2],[2,1],[2,2]]
Output: 1
Explanation: The above image depicts how the matrix changes each day starting from day 0.
The last day where it is possible to cross from top to bottom is on day 1.
Example 3:


Input: row = 3, col = 3, cells = [[1,2],[2,1],[3,3],[2,2],[1,1],[1,3],[2,3],[3,2],[3,1]]
Output: 3
Explanation: The above image depicts how the matrix changes each day starting from day 0.
The last day where it is possible to cross from top to bottom is on day 3.
 

Constraints:

2 <= row, col <= 2 * 104
4 <= row * col <= 2 * 104
cells.length == row * col
1 <= ri <= row
1 <= ci <= col
All the values of cells are unique.
'''
class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        def can_cross(t):
            mat = [[0]*col for _ in range(row)]
            for i in range(t):
                r, c = cells[i]
                mat[r-1][c-1] = 1
            q = deque([(0, i) for i in range(col) if not mat[0][i]])
            visited = [[False]*col for _ in range(row)]
            for i, j in q:
                visited[i][j] = True
            while q:
                i, j = q.popleft()
                if i == row - 1:
                    return True
                for di, dj in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                    ni, nj = i+di, j+dj
                    if 0<=ni<row and 0<=nj<col and not mat[ni][nj] and not visited[ni][nj]:
                        visited[ni][nj] = True
                        q.append((ni, nj))
            return False

        lo, hi = 0, row*col
        ans = 0
        while lo < hi:
            mid = lo + (hi-lo)//2
            if can_cross(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid

        if can_cross(lo): ans = lo
        return ans
