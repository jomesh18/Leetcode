'''
438. Find All Anagrams in a String
Medium

6238

235

Add to List

Share
Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
 

Constraints:

1 <= s.length, p.length <= 3 * 104
s and p consist of lowercase English letters.
Accepted
460,698
Submissions
970,598
'''

class Solution:
    def findAnagrams(self, s: str, p: str) -> [int]:
        P = Counter(p)
        S = Counter(s[:len(p)])
        res = []
        if P == S: res.append(0)
        for i in range(1, len(s)-len(p)+1):
            S[s[i-1]] -= 1
            if S[s[i-1]] == 0: S.pop(s[i-1])
            S[s[i+len(p)-1]] += 1
            if S == P: res.append(i)
        return res