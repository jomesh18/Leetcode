'''

'''
class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        while i < len(s) and s[i] == " ":
            i += 1
        sign = 1
        if i < len(s) and (s[i] == "-" or s[i] == "+"):
            if s[i] == "-":
                sign = -1
            i += 1
        ans = 0
        while i < len(s) and s[i].isdigit():
            ans = ans*10 + int(s[i])
            i += 1
        ans = ans * sign
        if ans>(2**31)-1:
            ans = 2**31-1
        elif ans < -2**31:
            ans = -2**31
        return ans

s = ""
Output: 0

sol = Solution()
print(sol.myAtoi(s))
