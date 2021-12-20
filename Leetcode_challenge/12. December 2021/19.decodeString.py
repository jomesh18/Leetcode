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
#                 stack.append("".join(temp[::-1])*int(digit[::-1]))
#             else:
#                 stack.append(c)
#         return "".join(stack)

# #leetcode, fastest recursive
# class Solution:
#     def decodeString(self, s: str) -> str:
#         def recursiveHelper(idx):
#             newIdx = idx + 1
#             while newIdx < len(s)-1 and s[newIdx].isnumeric():
#                 newIdx += 1
#             num = int(s[idx:newIdx])
#             res = ""
            
#             idx = newIdx + 1
            
#             while s[idx] != ']':
#                 if s[idx].isnumeric():
#                     subStr, newIdx = recursiveHelper(idx)
#                     res += subStr
#                     idx = newIdx + 1
#                 else:
#                     res += s[idx]
#                     idx += 1
            
#             return (num * res, idx)
            
            
#         s = "1[" + s + "]"

#         return recursiveHelper(0)[0]

#recurisve, my try
class Solution:
    def decodeString(self, s: str) -> str:

        def recursiveHelper(num_idx):
            num = 0
            while num_idx<len(s) and s[num_idx].isdigit():
                num = num*10+int(s[num_idx])
                num_idx += 1
            num_idx += 1
            string = []
            while num_idx < len(s) and s[num_idx] != ']':
                if s[num_idx].isdigit():
                    strin, i = recursiveHelper(num_idx)
                    string.append(strin)
                    num_idx = i
                else:
                    string.append(s[num_idx])
                    num_idx += 1
            num_idx += 1
            return ("".join(string)*num, num_idx)

        ans = []
        i = 0
        while i < len(s):
            if s[i].isdigit():
                stri, i = recursiveHelper(i)
                ans.append(stri)
            else:
                ans.append(s[i])
                i += 1
        return "".join(ans)


class Solution:
    def decodeString(self, s):
        stk, ans, n = [], "", ""
        for c in s:
            if c.isalpha():   ans += c
            elif c.isdigit(): n += c
            elif c == '[': 
                stk.append((n, ans))
                n, ans = "", ""
            else:
                cnt, prev = stk.pop()
                ans = prev + ans * int(cnt)
        return ans

s = "3[a]2[bc]"
Output = "aaabcbc"

s = "3[a2[c]]"
Output = "accaccacc"

s = "2[abc]3[cd]ef"
Output = "abcabccdcdcdef"

s = "abc3[cd]xyz"
Output = "abccdcdcdxyz"

s = "3[z]2[2[y]pq4[2[jk]e1[f]]]ef"
Output = "zzzyypqjkjkefjkjkefjkjkefjkjkefyypqjkjkefjkjkefjkjkefjkjkefef"

sol = Solution()
ans=sol.decodeString(s)
print(ans)
print(Output == ans)
