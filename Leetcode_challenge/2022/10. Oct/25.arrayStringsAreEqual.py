'''
1662. Check If Two String Arrays are Equivalent
Easy

1842

166

Add to List

Share
Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.

A string is represented by an array if the array elements concatenated in order forms the string.

 

Example 1:

Input: word1 = ["ab", "c"], word2 = ["a", "bc"]
Output: true
Explanation:
word1 represents string "ab" + "c" -> "abc"
word2 represents string "a" + "bc" -> "abc"
The strings are the same, so return true.
Example 2:

Input: word1 = ["a", "cb"], word2 = ["ab", "c"]
Output: false
Example 3:

Input: word1  = ["abc", "d", "defg"], word2 = ["abcddefg"]
Output: true
 

Constraints:

1 <= word1.length, word2.length <= 103
1 <= word1[i].length, word2[i].length <= 103
1 <= sum(word1[i].length), sum(word2[i].length) <= 103
word1[i] and word2[i] consist of lowercase letters.
'''
class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return ''.join(word1) == ''.join(word2)

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        def getchars(arr):
            for s in arr:
                for c in s:
                    yield c
            yield
        return all(c1 == c2 for c1, c2 in zip(getchars(word1), getchars(word2)))


#O(1) space
class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        word1p, word2p, s1p, s2p = 0, 0, 0, 0
        while word1p < len(word1) and word2p < len(word2):
            if word1[word1p][s1p] != word2[word2p][s2p]:
                return False
            s1p += 1
            s2p += 1
            if s1p == len(word1[word1p]):
                s1p = 0
                word1p += 1
            if s2p == len(word2[word2p]):
                s2p = 0
                word2p += 1
        return (word1p == len(word1) and word2p == len(word2))