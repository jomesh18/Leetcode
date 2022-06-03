'''
1654. Minimum Jumps to Reach Home
Medium

836

171

Add to List

Share
A certain bug's home is on the x-axis at position x. Help them get there from position 0.

The bug jumps according to the following rules:

It can jump exactly a positions forward (to the right).
It can jump exactly b positions backward (to the left).
It cannot jump backward twice in a row.
It cannot jump to any forbidden positions.
The bug may jump forward beyond its home, but it cannot jump to positions numbered with negative integers.

Given an array of integers forbidden, where forbidden[i] means that the bug cannot jump to the position forbidden[i], and integers a, b, and x, return the minimum number of jumps needed for the bug to reach its home. If there is no possible sequence of jumps that lands the bug on position x, return -1.

 

Example 1:

Input: forbidden = [14,4,18,1,15], a = 3, b = 15, x = 9
Output: 3
Explanation: 3 jumps forward (0 -> 3 -> 6 -> 9) will get the bug home.
Example 2:

Input: forbidden = [8,3,16,6,12,20], a = 15, b = 13, x = 11
Output: -1
Example 3:

Input: forbidden = [1,6,2,14,5,17,4], a = 16, b = 9, x = 7
Output: 2
Explanation: One jump forward (0 -> 16) then one jump backward (16 -> 7) will get the bug home.
 

Constraints:

1 <= forbidden.length <= 1000
1 <= a, b, forbidden[i] <= 2000
0 <= x <= 2000
All the elements in forbidden are distinct.
Position x is not forbidden.
'''
#recursion with memo
class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        forbidden = set(forbidden)
        visited = set()
        memo = {}
        stop = a+b+max(x, max(forbidden))
        def helper(i, back_once):
            if i < 0 or i > stop: return float("inf")
            if (i, back_once) in memo: return memo[(i, back_once)]
            if (i, back_once) in visited: return float("inf")
            visited.add((i, back_once))
            if i == x: return 0
            ans1, ans2 = float('inf'), float('inf')
            if i+a not in forbidden:
                ans1 = 1 + helper(i+a, False)
            if not back_once and i-b > 0 and i-b not in forbidden:
                ans2 = 1 + helper(i-b, True)
            ans = min(ans1, ans2)
            memo[(i, back_once)] = ans
            return ans
        ans = helper(0, False)
        return ans if ans != float('inf') else -1

