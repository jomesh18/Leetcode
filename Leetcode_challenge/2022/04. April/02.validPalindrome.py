'''
680. Valid Palindrome II
Easy

4807

271

Add to List

Share
Given a string s, return true if the s can be palindrome after deleting at most one character from it.

 

Example 1:

Input: s = "aba"
Output: true
Example 2:

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.
Example 3:

Input: s = "abc"
Output: false
 

Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.
Accepted
446,265
Submissions
1,145,392
'''
class Solution:
    def validPalindrome(self, s: str) -> bool:
        n = len(s)
        def helper(i, j, removedOne):
            if i >= j: return True
            if removedOne:
                if s[i] != s[j]:
                    return False
            else:
                if s[i] != s[j]:
                    return helper(i, j-1, True) or helper(i+1, j, True)
            return helper(i+1, j-1, removedOne)   
        return helper(0, n-1, False)

class Solution:
    def validPalindrome(self, s: str) -> bool:
        n = len(s)
        def check_pal(i, j):
            while i < j:
                if s[i] != s[j]: return False
                i += 1
                j -= 1
            return True
        i = 0
        for i in range(n//2):
            if s[i] != s[-1-i]:
                return check_pal(i, n-2-i) or check_pal(i+1, n-1-i)
        return True

s = "deeee"
Output: True