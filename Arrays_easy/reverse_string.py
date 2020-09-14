class Solution:
    def reverseString(self, s: [str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # s.reverse()
        front = 0
        back = len(s)-1
        while front<back:
            s[front], s[back] = s[back], s[front]
            front += 1
            back -= 1
        # n = len(s)
        # for i in range(n // 2):
        #     s[i],s[n-i-1] = s[n-i-1],s[i]

obj = Solution()
s = ['a', 'b', 'c', 'd']
print(s)
obj.reverseString(s)
print(s)
s = [""]
print(s)
obj.reverseString(s)
print(s)

# From leetcode, recursive solution
class Solution:
    def reverseString(self, s):
        def helper(left, right):
            if left < right:
                s[left], s[right] = s[right], s[left]
                helper(left + 1, right - 1)

        helper(0, len(s) - 1)
