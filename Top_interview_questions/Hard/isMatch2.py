'''
Regular Expression Matching

Solution
Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

'.' Matches any single character.​​​​
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

 

Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
 

Constraints:

1 <= s.length <= 20
1 <= p.length <= 30
s contains only lowercase English letters.
p contains only lowercase English letters, '.', and '*'.
It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.
'''
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        sn, pn = len(s), len(p)
        sp, pp = 0, 0
        memo = {}
        def dfs(sp, pp):
            if pp == pn:
                return sp == sn
            if (sp, pp) in memo: return memo[(sp, pp)]
            ans = False
            if sp < sn and s[sp] == p[pp] or p[pp] == '.':
                ans = dfs(sp+1, pp+1)
            elif p[pp] == '*':
                ans = dfs(sp, pp+1)
                if sp < sn and (s[sp] == p[pp-1] or p[pp-1] == '.'):
                    ans |= dfs(sp+1, pp)
            if pp < pn-1 and p[pp+1] == '*':
                ans |= dfs(sp, pp+2)
            memo[(sp, pp)] = ans
            return ans
        return dfs(0, 0)


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        sn, pn = len(s), len(p)
        sp, pp = 0, 0
        memo = {}
        def dfs(sp, pp):
            if (sp, pp) not in memo:
                if pp == pn:
                    memo[(sp, pp)] = sp == sn
                else:
                    first_match = sp < sn and p[pp] in {s[sp], '.'}
                    if pp < pn-1 and p[pp+1] == '*':
                        memo[(sp, pp)] = dfs(sp, pp+2) or (first_match and dfs(sp+1, pp))
                    else:
                        memo[(sp, pp)] = first_match and dfs(sp+1, pp+1)
            return memo[(sp, pp)]
        return dfs(0, 0)


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        sn, pn = len(s), len(p)
        dp = [[False]*(pn+1) for _ in range(sn+1)]
        dp[-1][-1] = True
        for sp in range(sn, -1, -1):
            for pp in range(pn-1, -1, -1):
                first_match = sp < sn and p[pp] in {s[sp], '.'}
                if pp < pn-1 and p[pp+1] == '*':
                    dp[sp][pp] = dp[sp][pp+2] or (first_match and dp[sp+1][pp])
                else:
                    dp[sp][pp] = first_match and dp[sp+1][pp+1]
        return dp[0][0]