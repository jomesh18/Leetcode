'''
Reverse Only Letters

Given a string s, reverse the string according to the following rules:

    All the characters that are not English letters remain in the same position.
    All the English letters (lowercase or uppercase) should be reversed.

Return s after reversing it.

 

Example 1:

Input: s = "ab-cd"
Output: "dc-ba"

Example 2:

Input: s = "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"

Example 3:

Input: s = "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"

 

Constraints:

    1 <= s.length <= 100
    s consists of characters with ASCII values in the range [33, 122].
    s does not contain '\"' or '\\'.

   Hide Hint #1  
This problem is exactly like reversing a normal string except that there are certain characters that we have to simply skip. That should be easy enough to do if you know how to reverse a string using the two-pointer approach.
'''
# class Solution:
#     def reverseOnlyLetters(self, s: str) -> str:
#         beg, end = 0, len(s)-1
#         res = [None] * len(s)
#         while beg < end:
#             if not (65<=ord(s[beg])<=90 or 97<=ord(s[beg])<=122):
#                 res[beg] = s[beg]
#                 beg += 1
#             elif not (65<=ord(s[end])<=90 or 97<=ord(s[end])<=122):
#                 res[end] = s[end]
#                 end -= 1
#             else:
#                 res[beg], res[end] = s[end], s[beg]
#                 beg += 1
#                 end -= 1
#         if beg == end:
#             res[beg] = s[beg]
#         return "".join(res)

#from leetcode
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        
        l, r = 0, len(s)-1
        
        res = list(s)
        
        while l < r:
            if not res[l].isalpha():
                l += 1
            elif not res[r].isalpha():
                r -= 1
            else:
                res[l], res[r] = res[r], res[l]
                
                l += 1
                r -= 1
                
        return ''.join(res)

s = "ab-cd"
# Output: "dc-ba"

s = "a-bC-dEf-ghIj"
# # Output: "j-Ih-gfE-dCba"

s = "Test1ng-Leet=code-Q!"
# Output: "Qedo1ct-eeLg=ntse-T!"

sol = Solution()
print(sol.reverseOnlyLetters(s))

