'''
792. Number of Matching Subsequences
Medium

4570

188

Add to List

Share
Given a string s and an array of strings words, return the number of words[i] that is a subsequence of s.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
 

Example 1:

Input: s = "abcde", words = ["a","bb","acd","ace"]
Output: 3
Explanation: There are three strings in words that are a subsequence of s: "a", "acd", "ace".
Example 2:

Input: s = "dsahjpjauf", words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
Output: 2
 

Constraints:

1 <= s.length <= 5 * 104
1 <= words.length <= 5000
1 <= words[i].length <= 50
s and words[i] consist of only lowercase English letters.
Accepted
190,401
Submissions
366,661
'''
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        d = defaultdict(list)
        for i, c in enumerate(s):
            d[c].append(i)
        res = 0
        for word in words:
            match = True
            prev = -1
            for c in word:
                if c not in d:
                    match = False
                    break
                l = d[c]
                ind = bisect.bisect_right(l, prev)
                if ind == len(l):
                    match = False
                    break
                else:
                    prev = l[ind]
            if match:
                res += 1
        return res


class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        d = defaultdict(list)
        for word in words:
            d[word[0]].append(word)
        count = 0
        for c in s:
            l = d[c]
            d[c] = []
            for w in l:
                if len(w) == 1:
                    count += 1
                else:
                    d[w[1]].append(w[1:])
        return count


class Solution(object):
    def numMatchingSubseq(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        word_dict = defaultdict(list)
        count = 0
        
        for word in words:
            word_dict[word[0]].append(word)            
        
        for char in S:
            words_expecting_char = word_dict[char]
            word_dict[char] = []
            for word in words_expecting_char:
                if len(word) == 1:
                    # Finished subsequence! 
                    count += 1
                else:
                    word_dict[word[1]].append(word[1:])
        
        return count