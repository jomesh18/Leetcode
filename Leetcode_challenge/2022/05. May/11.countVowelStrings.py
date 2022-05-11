'''
1641. Count Sorted Vowel Strings
Medium

2136

52

Add to List

Share
Given an integer n, return the number of strings of length n that consist only of vowels (a, e, i, o, u) and are lexicographically sorted.

A string s is lexicographically sorted if for all valid i, s[i] is the same as or comes before s[i+1] in the alphabet.

 

Example 1:

Input: n = 1
Output: 5
Explanation: The 5 sorted strings that consist of vowels only are ["a","e","i","o","u"].
Example 2:

Input: n = 2
Output: 15
Explanation: The 15 sorted strings that consist of vowels only are
["aa","ae","ai","ao","au","ee","ei","eo","eu","ii","io","iu","oo","ou","uu"].
Note that "ea" is not a valid string since 'e' comes after 'a' in the alphabet.
Example 3:

Input: n = 33
Output: 66045
 

Constraints:

1 <= n <= 50 
Accepted
99,721
Submissions
130,876
Seen this question in a real interview before?

Yes

No
'''
class Solution:
    def countVowelStrings(self, n: int) -> int:
        self.count = 0
        # self.res = []
        arr = ['a', 'e', 'i', 'o', 'u']
        def dfs(k, temp):
            if len(temp) == n:
                self.count += 1
                # self.res.append(''.join(temp))
                return

            for i in range(k, len(arr)):
                if i == len(arr)-1:
                    self.count += 1
                    return
                dfs(i, temp+[arr[i]])
                
        dfs(0, [])
        return self.count

#https://math.libretexts.org/Courses/Monroe_Community_College/MTH_220_Discrete_Math/7%3A_Combinatorics/7.5%3A_Combinations_WITH_Repetitions
class Solution:
    def countVowelStrings(self, n: int) -> int:
        return comb(n+4, n)

#dp
class Solution:
    def countVowelStrings(self, n: int) -> int:
        dp = [[1,1,1,1,1] for _ in range(n+1)]
        
        for i in range(1, n+1):
            for j in range(3, -1, -1):
                dp[i][j] = dp[i][j+1] + dp[i-1][j]
                
        return dp[n][0]
    