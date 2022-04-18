'''
Longest Palindromic Substring

Solution
Given a string s, return the longest palindromic substring in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
'''
#tle
# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         palindrome = ""
#         def is_palindrome(left, right):
#             while right > left:
#                 if s[left] != s[right]:
#                     return False
#                 left += 1
#                 right -= 1
#             return True

#         for i in range(len(s)):
#             for j in range(len(s)):
#                 if is_palindrome(i, j):
#                     if len(palindrome) < (j+1-i):
#                         palindrome = s[i:j+1]
#         return palindrome


#accepted
#slow, (>8000ms)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)  
        dp = [[False]*n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
        ans = [0,0]
        for i in range(n):
            for j in range(0, i+1):
                if i != j:
                    dp[j][i] = (s[i] == s[j] and (dp[j+1][i-1] if (j+1)<=(i-1) else True))
                if dp[j][i]:
                    # print(i, j)
                    if i-j+1 > ans[1]-ans[0]:
                        ans = [j, i]
        # print(dp)
        return s[ans[0]:ans[1]+1]


#accepted, dp, dp[l][i] is the string with length l and starting at pos i is palindrome or not
#slow, (>8000ms)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        ans = (1, 0)
        dp = [[False]*n for _ in range(n+1)]
        
        for l in range(1, n+1):
            for i in range(n-l+1):
                if l == 1: dp[l][i] = True
                elif l == 2: dp[l][i] = (s[i] == s[i+l-1])
                else: dp[l][i] = (s[i] == s[i+l-1] and dp[l-2][i+1])
                if dp[l][i]:
                    if l > ans[0]: ans = (l, i)
        # print(dp)
        # print(ans)
        return s[ans[1]: ans[1]+ans[0]]

#dp beautiful java solution
# public String longestPalindrome(String s) {
#   int n = s.length();
#   String res = null;
    
#   boolean[][] dp = new boolean[n][n];
    
#   for (int i = n - 1; i >= 0; i--) {
#     for (int j = i; j < n; j++) {
#       dp[i][j] = s.charAt(i) == s.charAt(j) && (j - i < 3 || dp[i + 1][j - 1]);
            
#       if (dp[i][j] && (res == null || j - i + 1 > res.length())) {
#         res = s.substring(i, j + 1);
#       }
#     }
#   }
    
#   return res;
# }

#expand from center, O(n*n), fastest (673ms)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        start = 0
        end = 0
        
        def expandfromcenter(i, j):
            while i >= 0 and j < n and s[i] == s[j]:
                i -= 1
                j += 1
            return j-i+1-2
        
        for i in range(n):
            l1 = expandfromcenter(i, i)
            l2 = expandfromcenter(i, i+1)
            l = max(l1, l2)
            if end-start < l:
                start = i -(l-1)//2
                end = i + l//2
        return s[start: end+1]

#two pointers, (506 ms) O(1) space, O(n*n) time
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        ans_ind = 0
        ans_len = 1
        for i in range(n):
            right = i
            while right < n and s[right] == s[i]:
                right += 1
            left = i-1
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            if ans_len < right-left-1:
                ans_len = right-left-1
                ans_ind = left+1
        return s[ans_ind: ans_ind+ans_len]

#above with comments
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        longest_palindrome_start, longest_palindrome_len = 0, 1

        for i in range(0, n):
            right = i
            while right < n and s[i] == s[right]:
                right += 1
            # s[i, right - 1] inclusive are equal characters e.g. "aaa"
            
            # while s[left] == s[right], s[left, right] inclusive is palindrome e.g. "baaab"
            left = i - 1
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            
            # s[left + 1, right - 1] inclusive is palindromic
            palindrome_len = right - left - 1
            if palindrome_len > longest_palindrome_len:
                longest_palindrome_len = palindrome_len
                longest_palindrome_start = left + 1
            
        return s[longest_palindrome_start: longest_palindrome_start + longest_palindrome_len]

s = "babad"

s="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
# res = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"

# s = "aacabdkacaa"
# # res = "aca"

print(len(s))

sol = Solution()
print(sol.longestPalindrome(s))
