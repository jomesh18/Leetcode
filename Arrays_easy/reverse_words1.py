class Solution:
    def reverseWords(self, s: str) -> str:
        # l = s.split()
        # l = l[::-1]
        # return " ".join(l)
        return " ".join(s.split()[::-1])

obj = Solution()
s = "the sky is blue"
print(s)
print(obj.reverseWords(s))
