'''
953. Verifying an Alien Dictionary
Easy

3731

1227

Add to List

Share
In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographically in this alien language.

 

Example 1:

Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
Example 2:

Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
Example 3:

Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).
 

Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 20
order.length == 26
All characters in words[i] and order are English lowercase letters.
'''
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        d = {c: i for i, c in enumerate(order)}
        for i in range(1, len(words)):
            curr, nex = words[i-1], words[i]
            min_len = min(len(curr), len(nex))
            if curr[:min_len] == nex[:min_len] and len(curr) > len(nex):
                # print('inside', i)
                return False
            for k in range(min_len):
                pos0, pos1 = d[curr[k]], d[nex[k]]
                if pos0 < pos1:
                    break
                elif pos0 == pos1:
                    continue
                elif pos0 > pos1:
                    # print('outside', i, k)
                    return False
        return True
