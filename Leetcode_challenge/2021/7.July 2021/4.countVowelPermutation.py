'''
Count Vowels Permutation
Given an integer n, your task is to count how many strings of length n can be formed under the following rules:

Each character is a lower case vowel ('a', 'e', 'i', 'o', 'u')
Each vowel 'a' may only be followed by an 'e'.
Each vowel 'e' may only be followed by an 'a' or an 'i'.
Each vowel 'i' may not be followed by another 'i'.
Each vowel 'o' may only be followed by an 'i' or a 'u'.
Each vowel 'u' may only be followed by an 'a'.
Since the answer may be too large, return it modulo 10^9 + 7.

 

Example 1:

Input: n = 1
Output: 5
Explanation: All possible strings are: "a", "e", "i" , "o" and "u".
Example 2:

Input: n = 2
Output: 10
Explanation: All possible strings are: "ae", "ea", "ei", "ia", "ie", "io", "iu", "oi", "ou" and "ua".
Example 3: 

Input: n = 5
Output: 68
 

Constraints:

1 <= n <= 2 * 10^4
   Hide Hint #1  
Use dynamic programming.
   Hide Hint #2  
Let dp[i][j] be the number of strings of length i that ends with the j-th vowel.
   Hide Hint #3  
Deduce the recurrence from the given relations between vowels.
'''

class Solution:
  def countVowelPermutation(self, n: int) -> int:
    dp = [[0 for _ in range(5)] for _ in range(n+1)]
    dp[1] = [1, 1, 1, 1, 1]
    for i in range(2, n+1):
      for j in range(5): #('a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4):
        if j == 0:
          dp[i][j] = dp[i-1][1] + dp[i-1][2]+dp[i-1][4]
        elif j == 1:
          dp[i][j] = dp[i-1][0]+dp[i-1][2]
        elif j == 2:
          dp[i][j] = dp[i-1][1]+dp[i-1][3]
        elif j == 3:
          dp[i][j] = dp[i-1][2]
        elif j == 4:
          dp[i][j] = dp[i-1][3]+dp[i-1][2]
    s = 0
    for num in dp[n]:
      s += num
    return s%(10**9+7)

n = 1
# Output: 5

n = 2
# # Output: 10

n = 5
# # Output: 68

s = Solution()
print(s.countVowelPermutation(n))
