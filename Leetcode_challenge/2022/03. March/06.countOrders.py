'''
1359. Count All Valid Pickup and Delivery Options
Hard

1384

128

Add to List

Share
Given n orders, each order consist in pickup and delivery services. 

Count all valid pickup/delivery possible sequences such that delivery(i) is always after of pickup(i). 

Since the answer may be too large, return it modulo 10^9 + 7.

 

Example 1:

Input: n = 1
Output: 1
Explanation: Unique order (P1, D1), Delivery 1 always is after of Pickup 1.
Example 2:

Input: n = 2
Output: 6
Explanation: All possible orders: 
(P1,P2,D1,D2), (P1,P2,D2,D1), (P1,D1,P2,D2), (P2,P1,D1,D2), (P2,P1,D2,D1) and (P2,D2,P1,D1).
This is an invalid order (P1,D2,P2,D1) because Pickup 2 is after of Delivery 2.
Example 3:

Input: n = 3
Output: 90
 

Constraints:

1 <= n <= 500
Accepted
47,755
Submissions
75,499
'''
class Solution:
    def countOrders(self, n: int) -> int:
        MOD = (10**9)+7
        memo = {}
        def total_ways(unpicked, undelivered):
            if not unpicked and not undelivered:
                return 1
            if unpicked < 0 or undelivered < 0 or unpicked > undelivered:
                return 0
            if (unpicked, undelivered) in memo: return memo[(unpicked, undelivered)]
            
            ans = 0
            ans += unpicked * total_ways(unpicked-1, undelivered)
            ans %= MOD
            
            ans += (undelivered-unpicked)*total_ways(unpicked, undelivered-1)
            ans %= MOD
            memo[(unpicked, undelivered)] = ans
            return ans
        return total_ways(n, n)

#dp
class Solution:
    def countOrders(self, n: int) -> int:
        MOD = (10**9)+7
        dp = [[0]*(n+1) for _ in range(n+1)]
        dp[0][0] = 1
        for unpicked in range(n+1):
            for undelivered in range(unpicked, n+1):
                if unpicked > 0:
                    dp[unpicked][undelivered] += unpicked * dp[unpicked-1][undelivered]
                dp[unpicked][undelivered] %= MOD
                if undelivered > unpicked:
                    dp[unpicked][undelivered] += (undelivered-unpicked)*dp[unpicked][undelivered-1]
                dp[unpicked][undelivered] %= MOD
        return dp[n][n]

#using permutations
class Solution:
    def countOrders(self, n: int) -> int:
        MOD = (10**9)+7
        ans = 1
        for i in range(1, n+1):
            ans *=  i
            ans %= MOD
            ans *= (2*i-1)
            ans %= MOD
        return ans

#using probability
class Solution:
    def countOrders(self, n: int) -> int:
        MOD = (10**9)+7
        ans = 1
        for i in range(1, 2*n+1):
            ans *= i
            if not i%2:
                ans //= 2
            ans %= MOD
        return ans