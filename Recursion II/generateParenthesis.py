'''
Generate Parentheses

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:

Input: n = 1
Output: ["()"]

 

Constraints:

    1 <= n <= 8

'''
#recursive
# class Solution:
#     def generateParenthesis(self, n: int) -> [str]:
#         res = []
#         def helper(lp, rp, temp):
#             # print(lp, rp)
#             if lp == 0 and rp == 0:
#                 res.append(temp)
#                 return
#             if lp == rp:
#                 helper(lp-1, rp, temp+"(")
#             elif lp < rp:
#                 helper(lp, rp-1, temp+")")
#                 if lp != 0:
#                     helper(lp-1, rp, temp+"(")
#         helper(n, n, "")
#         return res

#iterative
# class Solution:
#     def generateParenthesis(self, n: int) -> [str]:
#         res = []
#         stack = [(n, n, "")]
#         while stack:
#             lp, rp, temp = stack.pop()
#             if lp == 0 and rp == 0:
#                 res.append(temp)
#                 continue
#             if lp == rp:
#                 stack.append((lp-1, rp, temp+"("))
#             elif lp < rp:
#                 stack.append((lp, rp-1, temp+")"))
#                 if lp != 0:
#                     stack.append((lp-1, rp, temp+"("))
#         return res

#from leetcode, fastest
# class Solution:
#     def generateParenthesis(self, n: int) -> List[str]:
#         stack = []
#         res = []
#         num_left = 0
#         num_right = 0
        
#         def Parenthesis(stack, num_left, num_right):
            
#             if num_right == num_left == n:
#                 res.append(''.join(stack))
#                 return 
            
#             if num_right < num_left:
#                 stack.append(')')
#                 Parenthesis(stack, num_left, num_right+1)
#                 stack.pop()
                
#             if num_left < n:
#                 stack.append('(')
#                 Parenthesis(stack, num_left+1, num_right)
#                 stack.pop()
                
                
#         Parenthesis(stack, num_left, num_right)
#         return res

#from stefan
class Solution:
    def generateParenthesis(self, n):
        def generate(p, left, right, parens=[]):
            if left:         generate(p + '(', left-1, right)
            if right > left: generate(p + ')', left, right-1)
            if not right:    parens += p,
            return parens
        return generate('', n, n)

n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]

# n = 1
# Output: ["()"]

sol = Solution()
print(sol.generateParenthesis(n))
