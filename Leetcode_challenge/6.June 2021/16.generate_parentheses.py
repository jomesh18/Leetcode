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
#from leetcode solution
class Solution:
    def generateParenthesis(self, n: int) -> [str]:
        ans = []
        def backtrack(S = [], left = 0, right = 0):
            if len(S) == 2 * n:
                ans.append("".join(S))
                return
            if left < n:
                S.append("(")
                backtrack(S, left+1, right)
                S.pop()
            if right < left:
                S.append(")")
                backtrack(S, left, right+1)
                S.pop()
        backtrack()
        return ans

n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]

# n = 1
# # Output: ["()"]

s = Solution()
print(s.generateParenthesis(n))







# #Function for generating different permutations of the string  
# def generatePermutation(string,start,end):
#     #Prints the permutations
#     if(start == end-1):
#         print(string); 
#     else:
#         for current in range(start,end):

#        #Swapping the string by fixing a character
#             x = list(string);
#             x[start], x[current] = x[current], x[start]
  
#       #Recursively calling function generatePermutation() for rest of the characters  
  
#             generatePermutation("".join(x),start+1,end);  
#             #Swapping the string by fixing a character  
#             x[start], x[current] = x[current], x[start] 
  
# str = "ABC" 
# n = len(str)
# print("All the permutations of the string are: ") 
# generatePermutation(str,0,n)