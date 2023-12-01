'''
1662. Check If Two String Arrays are Equivalent
Solved
Easy
Topics
Companies
Hint
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
        # i, j, curr_i, curr_j = 0, 0, 0, 0
        # while i < len(word1) and j < len(word2):
        #     while i<len(word1) and curr_i == len(word1[i]):
        #         i += 1
        #         curr_i = 0
        #     while j<len(word2) and curr_j == len(word2[j]):
        #         j += 1
        #         curr_j = 0
        #     if i < len(word1) and j < len(word2):
        #         if word1[i][curr_i] != word2[j][curr_j]:
        #             return False
        #         curr_i += 1
        #         curr_j += 1
        # return (i == len(word1) and j == len(word2))

        return ''.join(word1) == ''.join(word2)