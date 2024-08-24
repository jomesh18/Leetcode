'''
1140. Stone Game II
Medium

3281

880

Add to List

Share
Alice and Bob continue their games with piles of stones.  There are a number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].  The objective of the game is to end with the most stones. 

Alice and Bob take turns, with Alice starting first.  Initially, M = 1.

On each player's turn, that player can take all the stones in the first X remaining piles, where 1 <= X <= 2M.  Then, we set M = max(M, X).

The game continues until all the stones have been taken.

Assuming Alice and Bob play optimally, return the maximum number of stones Alice can get.

 

Example 1:

Input: piles = [2,7,9,4,4]
Output: 10
Explanation:  If Alice takes one pile at the beginning, Bob takes two piles, then Alice takes 2 piles again. Alice can get 2 + 4 + 4 = 10 piles in total. If Alice takes two piles at the beginning, then Bob can take all three piles left. In this case, Alice get 2 + 7 = 9 piles in total. So we return 10 since it's larger. 
Example 2:

Input: piles = [1,2,3,4,5,100]
Output: 104
 

Constraints:

1 <= piles.length <= 100
1 <= piles[i] <= 104
'''
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        prefix_sum = [0]*(n+1)
        for i in range(n):
            prefix_sum[i+1] = prefix_sum[i] + piles[i]
        
        memo = {}
        def helper(i, M, turn):
            if i >= n: return 0
            if (i, M, turn) in memo: return memo[(i, M, turn)]
            if turn == 0:
                curr = 0
                for j in range(i, min(n, i+2*M)):
                    curr = max(curr, prefix_sum[j+1] - prefix_sum[i] + helper(j+1, max(M, j-i+1), 1))
            else:
                curr = float('inf')
                for j in range(i, min(n, i+2*M)):
                    curr = min(curr, helper(j+1, max(M, j-i+1), 0))
            memo[(i, M, turn)] = curr
            return curr
        return helper(0, 1, 0)