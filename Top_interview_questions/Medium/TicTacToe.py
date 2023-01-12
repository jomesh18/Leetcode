'''
https://www.codingninjas.com/codestudio/problem-details/design-tic-tac-toe_1265038
https://leetcode.ca/all/348.html
348. Design Tic-Tac-Toe
Design a Tic-tac-toe game that is played between two players on a n x n grid.

You may assume the following rules:

A move is guaranteed to be valid and is placed on an empty block.
Once a winning condition is reached, no more moves is allowed.
A player who succeeds in placing n of their marks in a horizontal, vertical, or diagonal row wins the game.
Example:
Given n = 3, assume that player 1 is "X" and player 2 is "O" in the board.

TicTacToe toe = new TicTacToe(3);

toe.move(0, 0, 1); -> Returns 0 (no one wins)
|X| | |
| | | |    // Player 1 makes a move at (0, 0).
| | | |

toe.move(0, 2, 2); -> Returns 0 (no one wins)
|X| |O|
| | | |    // Player 2 makes a move at (0, 2).
| | | |

toe.move(2, 2, 1); -> Returns 0 (no one wins)
|X| |O|
| | | |    // Player 1 makes a move at (2, 2).
| | |X|

toe.move(1, 1, 2); -> Returns 0 (no one wins)
|X| |O|
| |O| |    // Player 2 makes a move at (1, 1).
| | |X|

toe.move(2, 0, 1); -> Returns 0 (no one wins)
|X| |O|
| |O| |    // Player 1 makes a move at (2, 0).
|X| |X|

toe.move(1, 0, 2); -> Returns 0 (no one wins)
|X| |O|
|O|O| |    // Player 2 makes a move at (1, 0).
|X| |X|

toe.move(2, 1, 1); -> Returns 1 (player 1 wins)
|X| |O|
|O|O| |    // Player 1 makes a move at (2, 1).
|X|X|X|
Follow up:
Could you do better than O(n2) per move() operation?
'''
class Solution:
    def __init__(self, n):
        # Initialize your data structure here.
        self.rows = [0]*n
        self.cols = [0]*n
        self.diags = 0
        self.antidiags = 0
        self.n = n
#         print(self.rows, self.cols, self.diags, self.antidiags)
        
    def move(self, row, col, player):
        # Write your code here.
        delta = 3 - 2*player
        self.rows[row] += delta
        self.cols[col] += delta
        if row == col: self.diags += delta
        if row+col == self.n-1: self.antidiags += delta
#         print(self.rows, self.cols, self.diags, self.antidiags)
        if delta * self.n in [self.rows[row], self.cols[col], self.diags, self.antidiags]:
            return player
        return 0