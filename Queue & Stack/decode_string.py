'''
Decode String

Solution
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

 

Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"
Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"
Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
Example 4:

Input: s = "abc3[cd]xyz"
Output: "abccdcdcdxyz"
 

Constraints:

1 <= s.length <= 30
s consists of lowercase English letters, digits, and square brackets '[]'.
s is guaranteed to be a valid input.
All the integers in s are in the range [1, 300].
'''

# class Solution:
#     def decodeString(self, s: str) -> str:
#         stack = []
#         i = 0
#         while i < len(s):
#         	if s[i].isdigit():
#         		start = i
#         		while s[i].isdigit():
#         			i += 1
#         		stack.append(s[start: i])
#         		i -= 1
#         	elif s[i] == ']':
#         		temp = []
#         		while stack[-1] != '[':
#         			temp.append(stack.pop())
#         		stack.pop()
#         		if stack:
#         			if stack[-1].isdigit():
#         				temp *= int(stack.pop())
#         		# print(temp, stack)
#         		temp.reverse()
#         		stack.extend(temp)
#         	else:
#         		stack.append(s[i])
#         	i += 1
#        	res = []
#         while stack:
#         	res.append(stack.pop())
#         res.reverse()
#         return ''.join(res)

#from leetcode fastest solution

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curStr, count = '', 0
        for c in s:
            if c == '[':
                stack.append(curStr)
                stack.append(count)
                curStr, count = '', 0
            elif c == ']':
                preNum = stack.pop()
                preStr = stack.pop()
                curStr = preStr + preNum * curStr
            elif c.isdigit():
                count = count * 10 + int(c)
            else:
                curStr += c
        
        return curStr

#from leetcode

class Solution(object):
    def decodeString(self, s):
        stack = []
        stack.append(["", 1])
        num = ""
        for ch in s:
            if ch.isdigit():
              num += ch
            elif ch == '[':
                stack.append(["", int(num)])
                num = ""
            elif ch == ']':
                st, k = stack.pop()
                stack[-1][0] += st*k
            else:
                stack[-1][0] += ch
        return stack[0][0]


s = "3[a]2[bc]"
Output= "aaabcbc"
s = "3[a2[c]]"
Output= "accaccacc"
s = "2[abc]3[cd]ef"
Output= "abcabccdcdcdef"
s = "abc3[cd]xyz"
Output = "abccdcdcdxyz"

sol = Solution()
print(sol.decodeString(s)==Output)
