'''
https://www.lintcode.com/problem/746/
746 · Design Tic-Tac-Toe
OOD
Hard
Accepted Rate
39%
Description
Solution5
Notes10
Discuss4
Leaderboard
Record
Description
Design Tic-Tac-Toe game.

board has fixed size of 3
X always take the first move
If a place already got taken, and one player want to take that place,
an AlreadyTakenException will be thrown

If one player wins, and somebody try to make another move, a GameEndException will be thrown.
If all the places got taken,you should print "it's a draw"
If the winner shows up, return True
If tie or if there is no winner yet, return False
Example
Example 1:

Input:
move(0, 0) // X turn
move(1, 0) // O trun 
move(1, 1) // X turn
move(2, 0) // O turn
move(2, 2) // X turn and win
move(0, 0)  //throw GameEndException
move(0, 0) // X turn
move(0, 0) // throw AlreadyTakenException
move(1, 0) // O turn
move(1, 1) // X turn
move(2, 0) // o turn
move(2, 2) // X turn and win
Output:
x player wins!
x player wins!
'''
class TicTacToe {

    /** Initialize your data structure here. */
    public TicTacToe() {
        
    }
    
    public boolean move(int row, int col) throws AlreadyTakenException, GameEndException {
        
    }
}