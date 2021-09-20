'''
Find Winner on a Tic Tac Toe Game

Tic-tac-toe is played by two players A and B on a 3 x 3 grid.

Here are the rules of Tic-Tac-Toe:

    Players take turns placing characters into empty squares (" ").
    The first player A always places "X" characters, while the second player B always places "O" characters.
    "X" and "O" characters are always placed into empty squares, never on filled ones.
    The game ends when there are 3 of the same (non-empty) character filling any row, column, or diagonal.
    The game also ends if all squares are non-empty.
    No more moves can be played if the game is over.

Given an array moves where each element is another array of size 2 corresponding to the row and column of the grid where they mark their respective character in the order in which A and B play.

Return the winner of the game if it exists (A or B), in case the game ends in a draw return "Draw", if there are still movements to play return "Pending".

You can assume that moves is valid (It follows the rules of Tic-Tac-Toe), the grid is initially empty and A will play first.

 

Example 1:

Input: moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]
Output: "A"
Explanation: "A" wins, he always plays first.
"X  "    "X  "    "X  "    "X  "    "X  "
"   " -> "   " -> " X " -> " X " -> " X "
"   "    "O  "    "O  "    "OO "    "OOX"

Example 2:

Input: moves = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]
Output: "B"
Explanation: "B" wins.
"X  "    "X  "    "XX "    "XXO"    "XXO"    "XXO"
"   " -> " O " -> " O " -> " O " -> "XO " -> "XO " 
"   "    "   "    "   "    "   "    "   "    "O  "

Example 3:

Input: moves = [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]
Output: "Draw"
Explanation: The game ends in a draw since there are no moves to make.
"XXO"
"OOX"
"XOX"

Example 4:

Input: moves = [[0,0],[1,1]]
Output: "Pending"
Explanation: The game has not finished yet.
"X  "
" O "
"   "

 

Constraints:

    1 <= moves.length <= 9
    moves[i].length == 2
    0 <= moves[i][j] <= 2
    There are no repeated elements on moves.
    moves follow the rules of tic tac toe.
'''
class Solution:
    def tictactoe(self, moves: [[int]]) -> str:
        
        def win(moves):
            dic_row, dic_col = {}, {}
            for move in moves:
                row, col = move[0], move[1]
                dic_row[row] = dic_row.setdefault(row, 0) + 1
                dic_col[col] = dic_col.setdefault(col, 0) + 1
            # print(dic_row, dic_col)
            if 3 in dic_row.values(): return True
            if 3 in dic_col.values(): return True
            count = 0
            for move in moves:
                if move[0] == move[1]:
                    count += 1
            if count == 3: return True

            count = 0
            for move in moves:
                if move in [[0, 2], [2, 0], [1, 1]]:
                    count += 1
            if count == 3: return True
            return False

        if win(moves[::2]): return "A"
        elif win(moves[1::2]): return "B"
        elif len(moves) < 9: return "Pending"
        else: return "Draw"

moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]
# Output: "A"

# moves = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]
# # # Output: "B"

# moves = [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]
# # # Output: "Draw"

# moves = [[0,0],[1,1]]
# # # Output: "Pending"

moves = [[2,2],[0,2],[1,0],[0,1],[2,0],[0,0]]
# Output: "B"

sol = Solution()
print(sol.tictactoe(moves))
