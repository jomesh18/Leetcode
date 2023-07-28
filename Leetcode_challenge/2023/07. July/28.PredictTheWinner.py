'''
486. Predict the Winner
Medium

4393

200

Add to List

Share
You are given an integer array nums. Two players are playing a game with this array: player 1 and player 2.

Player 1 and player 2 take turns, with player 1 starting first. Both players start the game with a score of 0. At each turn, the player takes one of the numbers from either end of the array (i.e., nums[0] or nums[nums.length - 1]) which reduces the size of the array by 1. The player adds the chosen number to their score. The game ends when there are no more elements in the array.

Return true if Player 1 can win the game. If the scores of both players are equal, then player 1 is still the winner, and you should also return true. You may assume that both players are playing optimally.

 

Example 1:

Input: nums = [1,5,2]
Output: false
Explanation: Initially, player 1 can choose between 1 and 2. 
If he chooses 2 (or 1), then player 2 can choose from 1 (or 2) and 5. If player 2 chooses 5, then player 1 will be left with 1 (or 2). 
So, final score of player 1 is 1 + 2 = 3, and player 2 is 5. 
Hence, player 1 will never be the winner and you need to return false.
Example 2:

Input: nums = [1,5,233,7]
Output: true
Explanation: Player 1 first chooses 1. Then player 2 has to choose between 5 and 7. No matter which number player 2 choose, player 1 can choose 233.
Finally, player 1 has more score (234) than player 2 (12), so you need to return True representing player1 can win.
 

Constraints:

1 <= nums.length <= 20
0 <= nums[i] <= 107
'''
class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        memo = {}
        def helper(left, right, turn):
            if left > right: return 0
            if (left, right, turn) in memo: return memo[(left, right, turn)]
            ans = 0
            if turn == 1:
                ans = max(nums[left] + helper(left+1, right, 2), nums[right] + helper(left, right-1, 2))
            else:
                ans = min(-nums[left] + helper(left + 1, right, 1), -nums[right] + helper(left, right-1, 1))
            memo[(left, right, turn)] = ans
            return ans
        return helper(0, len(nums)-1, 1) >= 0


class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        memo = [[None]*n for _ in range(n)]
        def helper(left, right):
            if left > right: return 0
            if memo[left][right] is not None: return memo[left][right]
            l = nums[left] - helper(left+1, right)
            r = nums[right] - helper(left, right-1)
            memo[left][right] = max(l, r)
            return max(l, r)
        return helper(0, len(nums)-1) >= 0


class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [[0]*n for _ in range(n)]
        for i in range(n):
            dp[i][i] = nums[i]
        for diff in range(1, n):
            for i in range(n-diff):
                dp[i][i+diff] = max(nums[i] - dp[i+1][i+diff], nums[i+diff] - dp[i][i+diff-1])
        return dp[0][n-1] >= 0