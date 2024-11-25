'''
773. Sliding Puzzle
Hard

2258

60

Add to List

Share
On an 2 x 3 board, there are five tiles labeled from 1 to 5, and an empty square represented by 0. A move consists of choosing 0 and a 4-directionally adjacent number and swapping it.

The state of the board is solved if and only if the board is [[1,2,3],[4,5,0]].

Given the puzzle board board, return the least number of moves required so that the state of the board is solved. If it is impossible for the state of the board to be solved, return -1.

 

Example 1:


Input: board = [[1,2,3],[4,0,5]]
Output: 1
Explanation: Swap the 0 and the 5 in one move.
Example 2:


Input: board = [[1,2,3],[5,4,0]]
Output: -1
Explanation: No number of moves will make the board solved.
Example 3:


Input: board = [[4,1,2],[5,0,3]]
Output: 5
Explanation: 5 is the smallest number of moves that solves the board.
An example path:
After move 0: [[4,1,2],[5,0,3]]
After move 1: [[4,1,2],[0,5,3]]
After move 2: [[0,1,2],[4,5,3]]
After move 3: [[1,0,2],[4,5,3]]
After move 4: [[1,2,0],[4,5,3]]
After move 5: [[1,2,3],[4,5,0]]
 

Constraints:

board.length == 2
board[i].length == 3
0 <= board[i][j] <= 5
Each value board[i][j] is unique.
'''
class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        req = '123450'
        started = set()
        zero_pos = []
        curr = ''
        for i in range(2):
            for j in range(3):
                curr += str(board[i][j])
                if board[i][j] == 0:
                    zero_pos = (i, j)
        q = deque([(curr, zero_pos[0], zero_pos[1], 0)])
        visited = set()
        while q:
            curr, r, c, moves = q.popleft()
            if curr == req:
                return moves
            visited.add(curr)
            for dr, dc in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                nr, nc = r + dr, c + dc
                if 0<=nr<2 and 0<=nc<3:
                    old_pos = 3*r+c
                    new_pos = 3*nr+nc
                    min_ = min(old_pos, new_pos)
                    max_ = max(old_pos, new_pos)
                    new_curr = curr[:min_]+curr[max_]+curr[min_+1:max_]+curr[min_]+curr[max_+1:]
                    if new_curr not in visited:
                        q.append((new_curr, nr, nc, moves+1))
           
        return -1