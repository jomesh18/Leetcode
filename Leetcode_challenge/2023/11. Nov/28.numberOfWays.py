'''
2147. Number of Ways to Divide a Long Corridor
Solved
Hard
Topics
Companies
Hint
Along a long library corridor, there is a line of seats and decorative plants. You are given a 0-indexed string corridor of length n consisting of letters 'S' and 'P' where each 'S' represents a seat and each 'P' represents a plant.

One room divider has already been installed to the left of index 0, and another to the right of index n - 1. Additional room dividers can be installed. For each position between indices i - 1 and i (1 <= i <= n - 1), at most one divider can be installed.

Divide the corridor into non-overlapping sections, where each section has exactly two seats with any number of plants. There may be multiple ways to perform the division. Two ways are different if there is a position with a room divider installed in the first way but not in the second way.

Return the number of ways to divide the corridor. Since the answer may be very large, return it modulo 109 + 7. If there is no way, return 0.

 

Example 1:


Input: corridor = "SSPPSPS"
Output: 3
Explanation: There are 3 different ways to divide the corridor.
The black bars in the above image indicate the two room dividers already installed.
Note that in each of the ways, each section has exactly two seats.
Example 2:


Input: corridor = "PPSPSP"
Output: 1
Explanation: There is only 1 way to divide the corridor, by not installing any additional dividers.
Installing any would create some section that does not have exactly two seats.
Example 3:


Input: corridor = "S"
Output: 0
Explanation: There is no way to divide the corridor because there will always be a section that does not have exactly two seats.
 

Constraints:

n == corridor.length
1 <= n <= 105
corridor[i] is either 'S' or 'P'.
'''
class Solution:
    def numberOfWays(self, corridor: str) -> int:
        MOD = 10**9+7
        s_count = corridor.count('S')
        if s_count == 2: return 1
        if not s_count or s_count % 2: return 0
        s_count, last = 0, len(corridor)-1
        for i in range(len(corridor)-1, -1, -1):
            if corridor[i] == 'S':
                s_count += 1
                if s_count == 2:
                    last = i
                    break
        def helper(i):
            if i == last:
                return 1
            count = 0
            while i < last and count < 2:
                if corridor[i] == 'S':
                    count += 1
                i += 1
            ans = 1
            while i < last and corridor[i] == 'P':
                ans += 1
                i += 1
            return (ans * helper(i))%MOD

        return helper(0)


class Solution:
    def numberOfWays(self, corridor: str) -> int:
        MOD = 10**9+7
        s_indices = [i for i in range(len(corridor)) if corridor[i] == 'S']
        if not s_indices or len(s_indices) & 1: return 0
        ans = 1
        last_pair_second = 1
        for curr_pair_first in range(2, len(s_indices), 2):
            ans = (ans*(s_indices[curr_pair_first]-s_indices[last_pair_second]))%MOD
            last_pair_second += 2
        return ans