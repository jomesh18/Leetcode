'''
1653. Minimum Deletions to Make String Balanced
Medium

1569

47

Add to List

Share
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
s[i] is 'a' or 'b'
'''
class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        before_b = [0]*n
        for i in range(1, n):
            before_b[i] = before_b[i-1] + (1 if s[i-1] == 'b' else 0)
        after_a = [0]*n
        for i in range(n-2, -1, -1):
            after_a[i] = after_a[i+1] + (1 if s[i+1] == 'a' else 0)
        ans = n
        for i in range(n):
            ans = min(ans, before_b[i]+after_a[i])
        return ans
        