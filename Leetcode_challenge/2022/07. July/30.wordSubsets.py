'''
916. Word Subsets
Medium

1714

163

Add to List

Share
You are given two string arrays words1 and words2.

A string b is a subset of string a if every letter in b occurs in a including multiplicity.

For example, "wrr" is a subset of "warrior" but is not a subset of "world".
A string a from words1 is universal if for every string b in words2, b is a subset of a.

Return an array of all the universal strings in words1. You may return the answer in any order.

 

Example 1:

Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["e","o"]
Output: ["facebook","google","leetcode"]
Example 2:

Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["l","e"]
Output: ["apple","google","leetcode"]
 

Constraints:

1 <= words1.length, words2.length <= 104
1 <= words1[i].length, words2[i].length <= 10
words1[i] and words2[i] consist only of lowercase English letters.
All the strings of words1 are unique.
Accepted
72,489
Submissions
136,319
'''
class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        all_words2 = [0]*26
        for word in words2:
            w = [0]*26
            for c in word:
                w[ord(c)-ord('a')] += 1
            for i in range(26):
                all_words2[i] = max(all_words2[i], w[i])
        res = []
        for word in words1:
            w = [0]*26
            for c in word:
                w[ord(c)-ord('a')] += 1
            univ = True
            for i in range(26):
                if w[i] < all_words2[i]:
                    univ = False
                    break
            if univ:
                res.append(word)
        return res