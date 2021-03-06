# using library functions

# class Solution:
#     def reverseWords(self, s:str)->str:
#         # l = s.split()
#         # l = l[::-1]
#         # return " ".join(l)
#         return " ".join(s.split()[::-1])
			# return " ".join(reversed(s.spit()))
# obj = Solution()
# s = "the sky is blue"
# print(s)
# print(obj.reverseWords(s))

# without using split

# class Solution:
#     def reverseWords(self, s:str)->str:
#        	l = []
#        	res = []
#        	if s[0] != " ":
#        		l.append(s[0])
#        	for i in range(1, len(s)):
#        		if s[i]!= " ":
#        			l.append(s[i])
#        		elif s[i-1] != " ":
#        			res.append("".join(l))
#         		l.clear()
#         if s[-1] != ' ':
#           res.append("".join(l))
#         return " ".join(res[::-1])

# obj = Solution()
# s = "the sky  is blue "
# print(s)
# print(obj.reverseWords(s))

#Another attempt
# class Solution:
#     def reverseWords(self, s:str)->str:
#        	res = []
#        	start = 0
#        	for i in range(len(s)):
#        		if s[i] == " " and s[i-1] != " ":
#        			res.append(s[start: i])
#        			start = i+1
#        		elif s[i] == " ":
#        			start = i+1
#         if s[-1] != ' ' and start<len(s):
#           res.append(s[start:])
#         return " ".join(res[::-1])

# obj = Solution()
# s = "  the  sky  is blue"
# print(s)
# print(obj.reverseWords(s))
