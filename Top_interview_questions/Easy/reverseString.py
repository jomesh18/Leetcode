'''
Reverse String

Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

 

Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]

 

Constraints:

    1 <= s.length <= 105
    s[i] is a printable ascii character.

'''
class Solution:
    def reverseString(self, s:  [str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        lo, hi = 0, len(s) - 1
        while lo < hi:
            s[lo], s[hi] = s[hi], s[lo]
            lo += 1
            hi -= 1

#recursive
class Solution:
    def reverseString(self, s:  [str]) -> None:
        l = len(s)
        if l < 2:
            return s
        return self.reverseString(s[l//2:]) + self.reverseString(s[:l//2])

#classic
class Solution:
    def reverseString(self, s):
        for i in range(len(s)//2): s[i], s[-i-1] = s[-i-1], s[i]

#using bitwise inversion
class Solution:
    def reverseString(self, s):
        for i in range(len(s)//2): s[i], s[~i] = s[~i], s[i]