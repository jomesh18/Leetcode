'''
1128. Number of Equivalent Domino Pairs
Solved
Easy
Topics
Companies
Hint
Given a list of dominoes, dominoes[i] = [a, b] is equivalent to dominoes[j] = [c, d] if and only if either (a == c and b == d), or (a == d and b == c) - that is, one domino can be rotated to be equal to another domino.

Return the number of pairs (i, j) for which 0 <= i < j < dominoes.length, and dominoes[i] is equivalent to dominoes[j].

 

Example 1:

Input: dominoes = [[1,2],[2,1],[3,4],[5,6]]
Output: 1
Example 2:

Input: dominoes = [[1,2],[1,2],[1,1],[1,2],[2,2]]
Output: 3
 

Constraints:

1 <= dominoes.length <= 4 * 104
dominoes[i].length == 2
1 <= dominoes[i][j] <= 9
'''
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        dp = [[0]*11 for _ in range(11)]
        for i, j in dominoes:
            dp[i][j] += 1
            if i != j:
                dp[j][i] += 1
        ans = 0
        for i in range(1, 11):
            for j in range(i, 11):
                if dp[i][j] > 1:
                    n = dp[i][j]-1
                    ans += (n*(n+1))//2
        return ans
