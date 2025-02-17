'''
1079. Letter Tile Possibilities
Solved
Medium
Topics
Companies
Hint
You have n  tiles, where each tile has one letter tiles[i] printed on it.

Return the number of possible non-empty sequences of letters you can make using the letters printed on those tiles.

 

Example 1:

Input: tiles = "AAB"
Output: 8
Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".
Example 2:

Input: tiles = "AAABBC"
Output: 188
Example 3:

Input: tiles = "V"
Output: 1
 

Constraints:

1 <= tiles.length <= 7
tiles consists of uppercase English letters.
'''
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        ans = set()
        def helper(curr, rem):
            ans.add(curr)
            for i in range(len(rem)):
                new_rem = rem[:i]+rem[i+1:]
                helper(curr+rem[i], new_rem)
                helper(rem[i]+curr, new_rem)
        
        helper('', tiles)
        return len(ans)-1
