'''
1931. Painting a Grid With Three Different Colors
Solved
Hard
Topics
premium lock icon
Companies
Hint
You are given two integers m and n. Consider an m x n grid where each cell is initially white. You can paint each cell red, green, or blue. All cells must be painted.

Return the number of ways to color the grid with no two adjacent cells having the same color. Since the answer can be very large, return it modulo 109 + 7.

 

Example 1:


Input: m = 1, n = 1
Output: 3
Explanation: The three possible colorings are shown in the image above.
Example 2:


Input: m = 1, n = 2
Output: 6
Explanation: The six possible colorings are shown in the image above.
Example 3:

Input: m = 5, n = 5
Output: 580986
 

Constraints:

1 <= m <= 5
1 <= n <= 1000
'''
class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        colors = 'RGB'
        first_column_vals = []
        def get_vals(curr, first_column_vals):
            if len(curr) == m:
                first_column_vals.append(curr)
                return
            for c in colors:
                if curr and c == curr[-1]:
                    continue
                get_vals(curr+c, first_column_vals)

        get_vals('', first_column_vals)
        # print(first_column_vals)
        MOD = 10 ** 9 + 7
        memo = {}

        def solve(val_idx, remaining_cols, first_column_vals, MOD):
            if remaining_cols == 0:
                return 1
            if (val_idx, remaining_cols) in memo: return memo[(val_idx, remaining_cols)]
            prev_str = first_column_vals[val_idx]
            ways = 0
            for i in range(len(first_column_vals)):
                if i == val_idx:
                    continue
                curr_str = first_column_vals[i]
                valid = True
                for j in range(len(curr_str)):
                    if curr_str[j] == prev_str[j]:
                        valid = False
                        break
                if valid:
                    ways = (ways + solve(i, remaining_cols-1, first_column_vals, MOD)) % MOD
            
            memo[(val_idx, remaining_cols)] = ways
            return ways

        ans = 0
        for i in range(len(first_column_vals)):
            ways = solve(i, n-1, first_column_vals, MOD)
            ans = (ans + ways) % MOD
        return ans
