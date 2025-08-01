'''
2338. Count the Number of Ideal Arrays
Solved
Hard
Topics
premium lock icon
Companies
Hint
You are given two integers n and maxValue, which are used to describe an ideal array.

A 0-indexed integer array arr of length n is considered ideal if the following conditions hold:

Every arr[i] is a value from 1 to maxValue, for 0 <= i < n.
Every arr[i] is divisible by arr[i - 1], for 0 < i < n.
Return the number of distinct ideal arrays of length n. Since the answer may be very large, return it modulo 109 + 7.

 

Example 1:

Input: n = 2, maxValue = 5
Output: 10
Explanation: The following are the possible ideal arrays:
- Arrays starting with the value 1 (5 arrays): [1,1], [1,2], [1,3], [1,4], [1,5]
- Arrays starting with the value 2 (2 arrays): [2,2], [2,4]
- Arrays starting with the value 3 (1 array): [3,3]
- Arrays starting with the value 4 (1 array): [4,4]
- Arrays starting with the value 5 (1 array): [5,5]
There are a total of 5 + 2 + 1 + 1 + 1 = 10 distinct ideal arrays.
Example 2:

Input: n = 5, maxValue = 3
Output: 11
Explanation: The following are the possible ideal arrays:
- Arrays starting with the value 1 (9 arrays): 
   - With no other distinct values (1 array): [1,1,1,1,1] 
   - With 2nd distinct value 2 (4 arrays): [1,1,1,1,2], [1,1,1,2,2], [1,1,2,2,2], [1,2,2,2,2]
   - With 2nd distinct value 3 (4 arrays): [1,1,1,1,3], [1,1,1,3,3], [1,1,3,3,3], [1,3,3,3,3]
- Arrays starting with the value 2 (1 array): [2,2,2,2,2]
- Arrays starting with the value 3 (1 array): [3,3,3,3,3]
There are a total of 9 + 1 + 1 = 11 distinct ideal arrays.
 

Constraints:

2 <= n <= 104
1 <= maxValue <= 104
'''
class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        MOD = 10 ** 9 + 7
        m = min(n, 14)
        dp = [[0]*(m+1) for _ in range(maxValue+1)]
        # dp[i][j] shows how many arrays of length j ending with val i exists
        count = [0]*(m+1)
        for i in range(1, maxValue+1):
            dp[i][1] = 1
            count[1] += 1
            k = 2
            while i * k <= maxValue:
                for l in range(1, m):
                    dp[i*k][l+1] += dp[i][l]
                    count[l+1] += dp[i][l]
                k += 1
        
        # print(dp)
        # print(count)
        ans = 0
        fact = [1]*n
        for i in range(1, n):
            fact[i] = (fact[i-1]*i) % MOD
        inv_fact = [1]*n
        inv_fact[n-1] = pow(fact[n-1], MOD-2, MOD)
        for i in range(n-1, 0, -1):
            inv_fact[i-1] = (inv_fact[i] * i) % MOD

        for l in range(1, m+1):
            # ans = (ans + count[l] * nCr_mod(n-1, l-1, MOD)) % MOD
            # (n-1)!/(l-1)!/(n-l)!
            possibilities = (((fact[n-1]*inv_fact[l-1]) % MOD) * inv_fact[n-l])%MOD
            ans = (ans + (count[l]*possibilities) % MOD) % MOD

        return ans
