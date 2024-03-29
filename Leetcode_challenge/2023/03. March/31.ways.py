'''
1444. Number of Ways of Cutting a Pizza
Hard

1544

88

Add to List

Share
Given a rectangular pizza represented as a rows x cols matrix containing the following characters: 'A' (an apple) and '.' (empty cell) and given the integer k. You have to cut the pizza into k pieces using k-1 cuts. 

For each cut you choose the direction: vertical or horizontal, then you choose a cut position at the cell boundary and cut the pizza into two pieces. If you cut the pizza vertically, give the left part of the pizza to a person. If you cut the pizza horizontally, give the upper part of the pizza to a person. Give the last piece of pizza to the last person.

Return the number of ways of cutting the pizza such that each piece contains at least one apple. Since the answer can be a huge number, return this modulo 10^9 + 7.

 

Example 1:



Input: pizza = ["A..","AAA","..."], k = 3
Output: 3 
Explanation: The figure above shows the three ways to cut the pizza. Note that pieces must contain at least one apple.
Example 2:

Input: pizza = ["A..","AA.","..."], k = 3
Output: 1
Example 3:

Input: pizza = ["A..","A..","..."], k = 1
Output: 1
 

Constraints:

1 <= rows, cols <= 50
rows == pizza.length
cols == pizza[i].length
1 <= k <= 10
pizza consists of characters 'A' and '.' only.
'''
class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        rows, cols = len(pizza), len(pizza[0])
        apples = [[0]*(cols+1) for _ in range(rows+1)]
        for row in range(rows-1, -1, -1):
            for col in range(cols-1, -1, -1):
                apples[row][col] = ((pizza[row][col] == 'A') 
                                    +apples[row+1][col]
                                    +apples[row][col+1]
                                    -apples[row+1][col+1])
        
        dp = [[[0 for _ in range(cols)] for _ in range(rows)] for _ in range(k)]
        
        for row in range(rows):
            for col in range(cols):
                if apples[row][col]:
                    dp[0][row][col] = 1
        mod = (10 ** 9) + 7
        for rem in range(1, k):
            for row in range(rows):
                for col in range(cols):
                    val = 0
                    for next_row in range(row+1, rows):
                        if (apples[row][col] - apples[next_row][col]) > 0:
                            val += dp[rem-1][next_row][col]
                    for next_col in range(col+1, cols):
                        if (apples[row][col] - apples[row][next_col]) > 0:
                            val += dp[rem-1][row][next_col]
                    dp[rem][row][col] = val % mod

        return dp[k-1][0][0]