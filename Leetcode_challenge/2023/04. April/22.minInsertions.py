'''
1312. Minimum Insertion Steps to Make a String Palindrome
Hard

3639

48

Add to List

Share
Given a string s. In one step you can insert any character at any index of the string.

Return the minimum number of steps to make s palindrome.

A Palindrome String is one that reads the same backward as well as forward.

 

Example 1:

Input: s = "zzazz"
Output: 0
Explanation: The string "zzazz" is already palindrome we do not need any insertions.
Example 2:

Input: s = "mbadm"
Output: 2
Explanation: String can be "mbdadbm" or "mdbabdm".
Example 3:

Input: s = "leetcode"
Output: 5
Explanation: Inserting 5 characters the string becomes "leetcodocteel".
 

Constraints:

1 <= s.length <= 500
s consists of lowercase English letters.
'''
class Solution:
    def minInsertions(self, s: str) -> int:
        memo = {}
        def helper(l, r):
            if l >= r:
                return 0
            if (l, r) in memo: return memo[(l, r)]
            if s[l] == s[r]:
                ans = helper(l+1, r-1)
            else:
                ans = 1 + min(helper(l+1, r), helper(l, r-1))
            memo[(l, r)] = ans
            return ans
        return helper(0, len(s)-1)