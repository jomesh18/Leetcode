'''
1653. Minimum Deletions to Make String Balanced
Solved
Medium
Topics
premium lock icon
Companies
Hint
You are given a string s consisting only of characters 'a' and 'b'​​​​.

You can delete any number of characters in s to make s balanced. s is balanced if there is no pair of indices (i,j) such that i < j and s[i] = 'b' and s[j]= 'a'.

Return the minimum number of deletions needed to make s balanced.

 

Example 1:

Input: s = "aababbab"
Output: 2
Explanation: You can either:
Delete the characters at 0-indexed positions 2 and 6 ("aababbab" -> "aaabbb"), or
Delete the characters at 0-indexed positions 3 and 6 ("aababbab" -> "aabbbb").
Example 2:

Input: s = "bbaaaaabb"
Output: 2
Explanation: The only solution is to delete the first two characters.
 

Constraints:

1 <= s.length <= 105
s[i] is 'a' or 'b'​​.
'''
class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        b_before = [0]*(n+1)
        a_after = [0]*(n+1)
        for i in range(n):
            b_before[i+1] = b_before[i] + (1 if s[i] == 'b' else 0)
        for i in range(n-1, -1, -1):
            a_after[i] = a_after[i+1] + (1 if s[i] == 'a' else 0)
        # print(b_before)
        # print(a_after)
        ans = n
        for i in range(n):
            ans = min(ans, a_after[i] + b_before[i+1]-1)
        return ans
