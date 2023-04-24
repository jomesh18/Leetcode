'''
1416. Restore The Array
Hard

1387

47

Add to List

Share
A program was supposed to print an array of integers. The program forgot to print whitespaces and the array is printed as a string of digits s and all we know is that all integers in the array were in the range [1, k] and there are no leading zeros in the array.

Given the string s and the integer k, return the number of the possible arrays that can be printed as s using the mentioned program. Since the answer may be very large, return it modulo 109 + 7.

 

Example 1:

Input: s = "1000", k = 10000
Output: 1
Explanation: The only possible array is [1000]
Example 2:

Input: s = "1000", k = 10
Output: 0
Explanation: There cannot be an array that was printed this way and has all integer >= 1 and <= 10.
Example 3:

Input: s = "1317", k = 2000
Output: 8
Explanation: Possible arrays are [1317],[131,7],[13,17],[1,317],[13,1,7],[1,31,7],[1,3,17],[1,3,1,7]
 

Constraints:

1 <= s.length <= 105
s consists of only digits and does not contain leading zeros.
1 <= k <= 109
'''
class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        MOD = 10**9+7
        n = len(s)
        memo = {}
        def helper(i, curr):
            if curr > k: return 0
            if i == n: return 1 if (curr <= k and curr != 0) else 0
            if (i, curr) not in memo:
                ways = (helper(i+1, curr*10+int(s[i])))%MOD
                if s[i] != '0' and i != 0:
                    ways = (ways + helper(i+1, int(s[i])))%MOD
                memo[(i, curr)] = ways
            return memo[(i, curr)]
        return helper(0, 0)


class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        MOD = 10**9+7
        m, n = len(s), len(str(k))
        dp = [0]*m + [1]
        
        for i in range(m-1, -1, -1):
            count = 0
            if s[i] == '0': continue
            for end in range(i, m):
                curr = s[i: end+1]
                if int(curr) > k:
                    break
                count += dp[end + 1]
            dp[i] = (count) % MOD
      
        return dp[0]