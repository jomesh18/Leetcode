'''
N-Queens II

The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return the number of distinct solutions to the n-queens puzzle.

 

Example 1:

Input: n = 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown.

Example 2:

Input: n = 1
Output: 1

 

Constraints:

    1 <= n <= 9

'''
class Solution:
    def totalNQueens(self, n: int) -> int:
        assigned_cells = {}
        def backtrack_nqueen(row, count):
            for col in range(n):
                if not_under_attack(row, col):
                    # print(row, col, assigned_cells, count)
                    place_queen(row, col)
                    # print(row, col, assigned_cells, count)
                    if row + 1 == n:
                        count += 1
                    else:
                        count = backtrack_nqueen(row+1, count)
                        # print(count, self.assigned_cells)
                    revert_queen(row, col)
                    # print("reverted {}, {}, {}".format(row, col, assigned_cells))
            return count

        def not_under_attack(row, col):
            if (row, col) not in assigned_cells:
                return True

        def place_queen(row, col):
            # assigned_cells.update(find_cells(row, col))
            for elem in find_cells(row, col):
                assigned_cells[elem] = assigned_cells.get(elem, 0) + 1

        def find_cells(row, col):
            temp = set()
            for i in range(n):
                temp.add((row, i))
            for i in range(n):
                temp.add((i, col))
            i, j = row, col
            while i>=0 and j<n:
                temp.add((i, j))
                i -= 1
                j += 1
            i, j = row, col
            while i<n and j>=0:
                temp.add((i, j))
                i += 1
                j -= 1
            i, j = row, col
            while i<n and j<n:
                temp.add((i, j))
                i += 1
                j += 1
            i, j = row, col
            while i>=0 and j>=0:
                temp.add((i, j))
                i -= 1
                j -= 1
            return temp

        def revert_queen(row, col):
            for elem in find_cells(row, col):
                assigned_cells[elem] -= 1
                if assigned_cells[elem] == 0:
                    assigned_cells.pop(elem)

        return backtrack_nqueen(0, 0)

n = 4
# Output: 2

n = 1
Output: 1

sol = Solution()
print(sol.totalNQueens(n))
