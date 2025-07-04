'''
3333. Find the Original Typed String II
Solved
Hard
Topics
premium lock icon
Companies
Hint
Alice is attempting to type a specific string on her computer. However, she tends to be clumsy and may press a key for too long, resulting in a character being typed multiple times.

You are given a string word, which represents the final output displayed on Alice's screen. You are also given a positive integer k.

Return the total number of possible original strings that Alice might have intended to type, if she was trying to type a string of size at least k.

Since the answer may be very large, return it modulo 109 + 7.

 

Example 1:

Input: word = "aabbccdd", k = 7

Output: 5

Explanation:

The possible strings are: "aabbccdd", "aabbccd", "aabbcdd", "aabccdd", and "abbccdd".

Example 2:

Input: word = "aabbccdd", k = 8

Output: 1

Explanation:

The only possible string is "aabbccdd".

Example 3:

Input: word = "aaabbb", k = 3

Output: 8

 

Constraints:

1 <= word.length <= 5 * 105
word consists only of lowercase English letters.
1 <= k <= 2000
'''
class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        count = 1
        freq = []
        for i in range(1, len(word)):
            if word[i] == word[i-1]:
                count += 1
            else:
                freq.append(count)
                count = 1
        freq.append(count)

        M = 10**9+7
        P = 1
        for i in freq:
            P = (P * i) % M

        if k <= len(freq):
            return P
        if k > len(word):
            return 0
        if k == len(word):
            return 1
        n = len(freq)
        dp = [[0]*k for _ in range(n+1)]
        for i in range(k):
            dp[n][i] = 1
        
        for i in range(n-1, -1, -1):
            prefix_sum = [0]*(k+1)
            for h in range(1, k+1):
                prefix_sum[h] = (prefix_sum[h-1] + dp[i+1][h-1]) % M
            for count in range(k-1, -1, -1):
                l = count + 1
                r = count + freq[i]
                if r+1 > k:
                    r = k-1
                if l <= r:
                    dp[i][count] = (prefix_sum[r+1]-prefix_sum[l] + M ) % M

        invalid_cases = dp[0][0]
        return (P - invalid_cases + M ) % M
