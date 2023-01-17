'''
926. Flip String to Monotone Increasing
Medium

2881

122

Add to List

Share
A binary string is monotone increasing if it consists of some number of 0's (possibly none), followed by some number of 1's (also possibly none).

You are given a binary string s. You can flip s[i] changing it from 0 to 1 or from 1 to 0.

Return the minimum number of flips to make s monotone increasing.

 

Example 1:

Input: s = "00110"
Output: 1
Explanation: We flip the last digit to get 00111.
Example 2:

Input: s = "010110"
Output: 2
Explanation: We flip to get 011111, or alternatively 000111.
Example 3:

Input: s = "00011000"
Output: 2
Explanation: We flip to get 00000000.
 

Constraints:

1 <= s.length <= 105
s[i] is either '0' or '1'.
'''
class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        count = Counter(s)
        if '0' not in count or '1' not in count: return 0
        ans = min(count.values())
        memo = {}
        def helper(i, one_started):
            if i == len(s):
                return 0
            if (i, one_started) in memo: return memo[(i, one_started)]
            if one_started:
                if s[i] == '0':
                    ans = 1 + helper(i+1, one_started)
                else:
                    ans = helper(i+1, one_started)
            else:
                if s[i] == '1':
                    ans = 1 + helper(i+1, one_started)
                    ans = min(ans, helper(i+1, True))
                else:
                    ans = helper(i+1, one_started)
                    ans = min(ans, 1 + helper(i+1, True))
            memo[(i, one_started)] = ans
            return ans
        return helper(0, False)