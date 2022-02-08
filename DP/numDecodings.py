'''
 Decode Ways

Solution
A message containing letters from A-Z can be encoded into numbers using the following mapping:

'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:

"AAJF" with the grouping (1 1 10 6)
"KJF" with the grouping (11 10 6)
Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".

Given a string s containing only digits, return the number of ways to decode it.

The test cases are generated so that the answer fits in a 32-bit integer.

 

Example 1:

Input: s = "12"
Output: 2
Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: s = "226"
Output: 3
Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
Example 3:

Input: s = "06"
Output: 0
Explanation: "06" cannot be mapped to "F" because of the leading zero ("6" is different from "06").
 

Constraints:

1 <= s.length <= 100
s contains only digits and may contain leading zero(s).
'''
#accepted, memoization
class Solution:
    def numDecodings(self, s: str) -> int:
        l = len(s)
        if s[0] == "0": return 0
        dp = [0]*(len(s)+1)
        def helper(i):
            if i >= l : return 1
            if dp[i] != 0: return dp[i]
            count = 0
            if i+1 < l and 0 < int(s[i:i+2]) <= 26 and s[i] != "0" :
                count += helper(i+2)
            if 0 < int(s[i]) <= 26:                
                count += helper(i+1)
            dp[i] = count
            return count
        
        ans = helper(0)
        print(dp)
        return ans

#dp
class Solution:
    def numDecodings(self, s: str) -> int:
        l = len(s)
        if s[0] == "0": return 0
        dp = [0]*(len(s)+1)
        for i in range(l-1, -1, -1):
            

        def helper(i):
            if i >= l : return 1
            if dp[i] != 0: return dp[i]
            count = 0
            if i+1 < l and 0 < int(s[i:i+2]) <= 26 and s[i] != "0" :
                count += helper(i+2)
            if 0 < int(s[i]) <= 26:                
                count += helper(i+1)
            dp[i] = count
            return count
        
        ans = helper(0)
        print(dp)
        return ans


s = "12"
# Output: 2

s = "226"
# # Output: 3

# s = "06"
# Output: 0

s = "".join([str(i) for i in range(1, 10)])
#

s = "2101"
#Output: 1

sol = Solution()
print(sol.numDecodings(s))
