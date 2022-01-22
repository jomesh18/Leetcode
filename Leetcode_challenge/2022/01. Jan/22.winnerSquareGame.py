'''
1510. Stone Game IV
Hard

842

36

Add to List

Share
Alice and Bob take turns playing a game, with Alice starting first.

Initially, there are n stones in a pile. On each player's turn, that player makes a move consisting of removing any non-zero square number of stones in the pile.

Also, if a player cannot make a move, he/she loses the game.

Given a positive integer n, return true if and only if Alice wins the game otherwise return false, assuming both players play optimally.

 

Example 1:

Input: n = 1
Output: true
Explanation: Alice can remove 1 stone winning the game because Bob doesn't have any moves.
Example 2:

Input: n = 2
Output: false
Explanation: Alice can only remove 1 stone, after that Bob removes the last one winning the game (2 -> 1 -> 0).
Example 3:

Input: n = 4
Output: true
Explanation: n is already a perfect square, Alice can win with one move, removing 4 stones (4 -> 0).
 

Constraints:

1 <= n <= 105
Accepted
41,505
Submissions
68,540

'''
'''
Intuition

First, let's analyze the problem.

According to Zermelo's_theorem, given n stones, either Alice has a must-win strategy, or Bob has one. Therefore, for Alice, the current state is either "must-win" or "must-lose". But how to determine which one it is?

For convenience, in the following context, "the current player" refers to the player now removing the stones, and "state i" refers to when there is i stones remaining.

Now the problem asks whether the current player will win in state n.

If we can go to a known state where Bob must lose, then we know Alice must win in the current state. All Alice has to do is to move the corresponding number of stones to go to that state. Therefore we need to find out which state Bob must lose.

Note that after going to the next state, Bob becomes the player removing the stones, which is the position of Alice in the current state. Therefore, to find out whether Bob will lose in the next state, we just need to check whether our function gives False for remaining stones.
'''

class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [False] * (n+1)
        perfect_factors_set = set(i*i for i in range(1, int(n**.5)+1))
        for i in range(1, n+1):
            perfect_factors = [j for j in perfect_factors_set if j <= i]
            dp[i] = any([not dp[i-k] for k in perfect_factors])
        return dp[n]

sol = Solution()
print(sol.winnerSquareGame(n))
