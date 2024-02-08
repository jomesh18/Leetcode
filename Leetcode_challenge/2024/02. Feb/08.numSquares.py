'''
279. Perfect Squares
Medium

10482

429

Add to List

Share
Given an integer n, return the least number of perfect square numbers that sum to n.

A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.

 

Example 1:

Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
 

Constraints:

1 <= n <= 104
'''
class Solution:
    def numSquares(self, n: int) -> int:
        squares = []
        for i in range(1, n):
            sq = i*i
            if sq <= n:
                squares.append(sq)
            else:
                break
        memo = {}
        def helper(curr):
            if curr < 0:
                return n
            if curr == 0:
                return 0
            if curr in memo: return memo[curr]
            ans = n
            for sq in squares:
                if curr-sq >= 0:
                    ans = min(ans, 1+helper(curr-sq))
                else:
                    break
            memo[curr] = ans
            return ans
        return helper(n)
    

class Solution:
    def numSquares(self, n: int) -> int:
        squares = [i*i for i in range(1, int(sqrt(n))+1)]
        q = deque([(n, 0)])
        visited = [False]*(n+1)
        visited[n] = True
        while q:
            curr, step = q.popleft()
            if curr == 0:
                return step
            for sq in squares:
                if curr-sq >= 0:
                    if not visited[curr-sq]:
                        q.append((curr-sq, step+1))
                        visited[curr-sq] = True
                else:
                    break
        
            