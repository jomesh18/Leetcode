'''
Wildcard Matching

Solution
Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*' where:

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

 

Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input: s = "aa", p = "*"
Output: true
Explanation: '*' matches any sequence.
Example 3:

Input: s = "cb", p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
 

Constraints:

0 <= s.length, p.length <= 2000
s contains only lowercase English letters.
p contains only lowercase English letters, '?' or '*'.
'''
# recursive
# O(m*n) where m is len(s) and n is len(p)
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
            if sp < sn and (s[sp] == p[pp] or p[pp] == '?'):
                ans = dfs(sp+1, pp+1)
            elif p[pp] == '*':
                ans = dfs(sp, pp+1) or (sp < sn and dfs(sp+1, pp))
            memo[(sp,pp)] = ans
            return ans
        return dfs(0, 0)

# iterative,  O(1) space
# O(m*n) where m is len(s) and n is len(p)
class Solution:
    def isMatch(self, s: str, p: str) -> bool:    
        sn, pn = len(s), len(p)
        sp, pp = 0, 0
        star_idx, match_idx = -1, 0
        while sp < sn:
            # advancing both pointers
            if pp < pn and (s[sp] == p[pp] or p[pp] == '?'):
                sp += 1
                pp += 1
            # found star, advancing p pointer
            elif pp < pn and p[pp] == '*':
                match_idx = sp
                star_idx = pp
                pp += 1
            # previous was star, so advancing s pointer
            elif star_idx != -1:
                match_idx += 1
                sp = match_idx
                pp = star_idx + 1
            # current p not star, previous was not star, characters dont match
            else: 
                return False
        while pp < pn and p[pp] == '*':
            pp += 1
        return pp == pn

# dp approach
class Solution:
    def isMatch(self, s: str, p: str) -> bool:    
        dp = [[False]*(len(p)+1) for _ in range(len(s)+1)]
        
        for j in range(1, len(p)+1):
            if p[j-1] != '*':
                break
            dp[0][j] = True
            
        dp[0][0] = True
        
        for i in range(1, len(s)+1):
            for j in range(1, len(p)+1):
                if s[i-1] == p[j-1] or p[j-1] == '?':
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    dp[i][j] = dp[i][j-1] or dp[i-1][j]
        return dp[-1][-1]
