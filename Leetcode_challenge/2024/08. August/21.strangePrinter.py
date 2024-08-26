'''
664. Strange Printer
Hard

2629

279

Add to List

Share
There is a strange printer with the following two special properties:

The printer can only print a sequence of the same character each time.
At each turn, the printer can print new characters starting from and ending at any place and will cover the original existing characters.
Given a string s, return the minimum number of turns the printer needed to print it.

 

Example 1:

Input: s = "aaabbb"
Output: 2
Explanation: Print "aaa" first and then print "bbb".
Example 2:

Input: s = "aba"
Output: 2
Explanation: Print "aaa" first and then print "b" from the second place of the string, which will cover the existing character 'a'.
 

Constraints:

1 <= s.length <= 100
s consists of lowercase English letters.
'''
class Solution:
    def strangePrinter(self, s: str) -> int:
        memo = {}
        def solve(l, r):
            if l > r: return 0
            if (l, r) in memo: return memo[(l, r)]
            cost = 1 + solve(l, r-1)
            for i in range(l, r):
                if s[i] == s[r]:
                    cost = min(cost, solve(l, i) + solve(i+1, r-1))
            memo[(l, r)] = cost
            return cost
        return solve(0, len(s)-1)