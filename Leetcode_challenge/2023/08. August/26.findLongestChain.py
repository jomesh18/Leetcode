'''
646. Maximum Length of Pair Chain
Medium

3693

124

Add to List

Share
You are given an array of n pairs pairs where pairs[i] = [lefti, righti] and lefti < righti.

A pair p2 = [c, d] follows a pair p1 = [a, b] if b < c. A chain of pairs can be formed in this fashion.

Return the length longest chain which can be formed.

You do not need to use up all the given intervals. You can select pairs in any order.

 

Example 1:

Input: pairs = [[1,2],[2,3],[3,4]]
Output: 2
Explanation: The longest chain is [1,2] -> [3,4].
Example 2:

Input: pairs = [[1,2],[7,8],[4,5]]
Output: 3
Explanation: The longest chain is [1,2] -> [4,5] -> [7,8].
 

Constraints:

n == pairs.length
1 <= n <= 1000
-1000 <= lefti < righti <= 1000
'''
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x:(x[0], x[1]))
        n = len(pairs)
        memo = {}
        def helper(i, prev):
            if i == n:
                return 0
            if (i, prev) in memo: return memo[(i, prev)]
            ans = helper(i+1, prev)
            if prev == -1 or (prev != -1 and pairs[prev][1] < pairs[i][0]):
                ans = max(ans, 1 + helper(i+1, i))
            memo[(i, prev)] = ans
            return ans
        return helper(0, -1)


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x:x[1])
        ans = 0
        curr = float('-inf')
        for a, b in pairs:
            if a > curr:
                ans += 1
                curr = b
        return ans