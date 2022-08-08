'''
1220. Count Vowels Permutation
Hard

2248

150

Add to List

Share
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
Accepted
91,945
Submissions
150,581
'''
class Solution:
    def countVowelPermutation(self, n: int) -> int:
        mod = 10**9+7
        if n == 1: return 5
        count = [1]*5
        d = {0: 1, 1: 2, 2: 4, 3: 2, 4: 1}
        next_l = {0: [1], 1: [0, 2], 2: [0, 1, 3, 4], 3: [2, 4], 4: [0]}
        n -= 2
        while n:
            t = [0]*5
            for i in range(5):
                for v in next_l[i]:
                    t[v] += count[i]
            count = t[:]
            n -= 1
        # print(count)
        return sum(count[i]*d[i] for i in range(len(count)))%mod

class Solution:
    def countVowelPermutation(self, n: int) -> int:
        mod = 10**9+7
        a, e, i, o, u = 1, 1, 1, 1, 1
        for _ in range(n-1):
            a, e, i, o, u = e, a+i, a+e+o+u, i+u, a
        return (a+e+i+o+u) % mod
    