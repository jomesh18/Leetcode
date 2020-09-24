class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join([element[::-1] for element in s.split()])

obj = Solution()
s = "Let's take LeetCode contest"
print(s)
print(obj.reverseWords(s))
