'''
Perfect Squares

Solution
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

1 <= n <= 10^4
'''
# memory error
# from math import sqrt
# from collections import deque
# class Solution:
#     def numSquares(self, n: int) -> int:
#         nodes = [i*i for i in range(1, int(sqrt(n))+1)]
#         step = -1
#         q = deque([0])
#         while q:
#             l = len(q)
#             step += 1
#             for _ in range(l):
#                 c = q.popleft()
#                 if c == n: return step
#                 q.extend([c+node for node in nodes if c+node <= n])


# from collections import deque
# class Solution:
#     def numSquares(self, n: int) -> int:
#         step = -1
#         q = deque([n])
#         visited = [0]*n
#         while q:
#             l = len(q)
#             step += 1
#             for _ in range(l):
#                 c = q.popleft()
#                 if c == 0: return step
#                 for node in range(1, int(c**.5)+1):
#                     path = c-node*node
#                     if path>=0 and visited[path] == 0:
#                         visited[path] = 1
#                         q.append(path)

#from leetcode, dp solution, using static, stefanpoch
# class Solution(object):
#     _dp = [0]
#     def numSquares(self, n):
#         dp = self._dp
#         while len(dp) <= n:
#             dp += min(dp[-i*i] for i in range(1, int(len(dp)**0.5+1))) + 1,
#         return dp[n]

'''
from leetcode, another dp solution
First solution is to use DP.
Suppose dp[i] records to least number of perfect square numbers that sum up to i. And there are multiple ways for perfect square numbers to sum up to i.
The candidate way is to add a perfect square number j*j to a sum of perfect square numbers that equals to i. And it can be generized as i-j*j + j*j. So the least number of perfect square numbers that sum up to i-j*j is dp[i-j*j]. So candidate answer is dp[i-j*j]+1(add one more number j*j).
So for dp[i], we just pick the minimum of all candidates:

dp[i] = min(dp[i-j*j] for j in range(1, int(i**0.5)+1)) + 1
Time complexity is O(n√n). Actually running time is 2500ms.
'''
class Solution:
    def numSquares(self, n):
        dp = [0] + [float('inf')]*n
        for i in range(1, n+1):
            dp[i] = min(dp[i-j*j] for j in range(1, int(i**0.5)+1)) + 1
        return dp[n]

'''
Another solution is to use BFS.
The root node is n, and we are trying to keep reduce a perfect square number from it each layer. So the next layer nodes are {n - i**2 for i in range(1, int(n**0.5)+1)}. And target leaf node is 0, indicates n is made up of a number of perfect square numbers and depth is the least number of perfect square numbers.
'''

# class Solution:
#     def numSquares(self, n):
#         squares = [i**2 for i in range(1, int(n**0.5)+1)]
#         d, q, nq = 1, {n}, set()
#         while q:
#             for node in q:
#                 for square in squares:
#                     if node == square: return d
#                     if node < square: break
#                     nq.add(node-square)
#             q, nq, d = nq, set(), d+1

'''
Each while loop takes Si, which is the number of the values that is within range {1, n} whose least number of perfect squares is i. E.g. S1 = √n.
So total time cost should be c∑Si = cS1+cS2+...+cSd. Since I used a set for queue here, ∑Si ≤ n, and time complexity is O(n). The worst case would be n happen to have a larger least number of perfect square than any number from {1, n-1}. Actually running time is 220ms.
'''

'''
from leetcode, math solution
First of all, there is a statement that any number can be represented as sum of 4 squares:
https://en.wikipedia.org/wiki/Lagrange's_four-square_theorem. So, answer always will be 4? No, when we talk about 4 squares, it means that some of them can be equal to zero. So, we have 4 options: either 1, 2, 3 or 4 squares and we need to choose one of these numbers.

How to check if number is full square? Just compare square of integer part of root and this number. Complexity of this part is O(1).
How to check if number is sum of 2 squares: n = i*i + j*j? iterate ovell all i < sqrt(n) and check that n - i*i is full square. Complexity of this part is O(sqrt(n)).
How to check that number is sum of 4 squares? In the same link for wikipedia:
by proving that a positive integer can be expressed as the sum of three squares if and only if it is not of the form 4^k(8m+7) for integers k and m. So, what we need to do is to check this condition and return true if it fulfilled. Complexity is O(log n)
Do we need to check anything else? No, because we have only one options left: 3 squares.
Complexity: time complexity is O(sqrt(n)) and space complexity is O(1).
Further discussion. What if you do not know this 4^k(8m+7) formula on real interview? Then you need to check if number is sum of 3 squares by hands: n = i*i + j*j + k*k with complexity O(n): we check all pairs i,j < sqrt(n). What if we do not know, that each number is sum of 4 squares? Then we need to check also possible sums of 4 squares with complexity O(n sqrt(n)).
'''
# class Solution:
#     def numSquares(self, n):
#         if int((n)**.5)**2 == n: return 1
#         for j in range(int((n)**.5) + 1):
#             if int((n - j*j)**.5)**2 == n - j*j: return 2
            
#         while n % 4 == 0: 
#             n >>= 2
#         if n % 8 == 7: return 4
#         return 3


# n = 12
# # Output: 3
# # Explanation: 12 = 4 + 4 + 4.
# n = 13
# # Output: 2
# # Explanation: 13 = 4 + 9.
# n = 1
# # Output: 1
# n = 104
# # Output: 2
n = 7168
# # Output: 

s = Solution()
print(s.numSquares(n))
