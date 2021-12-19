'''
394. Decode String
Medium

6855

299

Add to List

Share
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
Accepted
419,889
Submissions
759,293
'''
# not working 
# class Solution:
#     def decodeString(self, s: str) -> str:
#         stack = []
#         res = []
#         for c in s:
#             if c == ']':
#                 temp = []
#                 while stack[-1] != '[':
#                     temp.append(stack.pop())
#                 stack.pop()
#                 digit = ""
#                 while stack and stack[-1].isdigit():
#                     digit += stack.pop()
#                 stack.append("".join(temp)[::-1]*int(digit[::-1]))
#             else:
#                 stack.append(c)
#         return "".join(stack)


class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        i = 0
        while i < len(s):
            if s[i].isdigit():
                start = i
                while s[i].isdigit():
                    i += 1
                stack.append(s[start: i])
                i -= 1
            elif s[i] == ']':
                temp = []
                while stack[-1] != '[':
                    temp.append(stack.pop())
                stack.pop()
                if stack:
                    if stack[-1].isdigit():
                        temp *= int(stack.pop())
                # print(temp, stack)
                temp.reverse()
                stack.extend(temp)
            else:
                stack.append(s[i])
            i += 1
        res = []
        while stack:
            res.append(stack.pop())
        res.reverse()
        return ''.join(res)

s = "3[a]2[bc]"
# Output: "aaabcbc"

s = "3[a2[c]]"
# # Output: "accaccacc"

s = "2[abc]3[cd]ef"
# # Output: "abcabccdcdcdef"

s = "abc3[cd]xyz"
# Output: "abccdcdcdxyz"

s = "3[z]2[2[y]pq4[2[jk]e1[f]]]ef"
# Output: "zzzyypqjkjkefjkjkefjkjkefjkjkefyypqjkjkefjkjkefjkjkefjkjkefef"

sol = Solution()
print(sol.decodeString(s))
