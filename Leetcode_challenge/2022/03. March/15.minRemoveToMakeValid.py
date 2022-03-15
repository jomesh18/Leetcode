'''

'''
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        for c in s:
            if c == ")":
                temp = []
                while stack and stack[-1] != "(":
                    temp.append(stack.pop())
                if stack:
                    temp.append(stack.pop())
                    stack.append("".join(temp[::-1])+c)
                else:
                    stack.append(''.join(temp[::-1]))
            else:
                stack.append(c)
        count = 0
        res = []
        while stack:
            c = stack.pop()
            if c == '(':
                count -= 1
            elif c == ')':
                count += 1
            if count < 0:
                count += 1
            else:
                res.append(c)
        return "".join(res[::-1])

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        count = 0
        for c in s:
            if c == ")":
                count -= 1
            elif c == '(':
                count += 1
            if count < 0:
                count += 1
            else:
                stack.append(c)
        count = 0
        res = []
        while stack:
            c = stack.pop()
            if c == '(':
                count -= 1
            elif c == ')':
                count += 1
            if count < 0:
                count += 1
            else:
                res.append(c)
        return "".join(res[::-1])

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        l_s = list(s)
        stack = []
        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
            elif c == ")":
                if stack: stack.pop()
                else: l_s[i] = ""
        while stack:
            l_s[stack.pop()] = ""
            
        return "".join(l_s)