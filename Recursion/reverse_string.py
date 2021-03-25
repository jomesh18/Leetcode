'''
Reverse String

Write a function that reverses a string. The input string is given as an array of characters s.

 

Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]

 

Constraints:

    1 <= s.length <= 105
    s[i] is a printable ascii character.

 

Follow up: Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

'''

class Solution:
    def reverseString(self, s: []) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def rev(start, end):
        	if start >= end:
        		return
        	s[start], s[end] = s[end], s[start]
        	rev(start+1, end-1)
        rev(0, len(s)-1)
        return s

# s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]

s = ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]
print(s)
sol = Solution()
print(sol.reverseString(s))
