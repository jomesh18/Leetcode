'''
318. Maximum Product of Word Lengths
Medium

2342

102

Add to List

Share
Given a string array words, return the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. If no such two words exist, return 0.

 

Example 1:

Input: words = ["abcw","baz","foo","bar","xtfn","abcdef"]
Output: 16
Explanation: The two words can be "abcw", "xtfn".
Example 2:

Input: words = ["a","ab","abc","d","cd","bcd","abcd"]
Output: 4
Explanation: The two words can be "ab", "cd".
Example 3:

Input: words = ["a","aa","aaa","aaaa"]
Output: 0
Explanation: No such pair of words.
 

Constraints:

2 <= words.length <= 1000
1 <= words[i].length <= 1000
words[i] consists only of lowercase English letters.
'''
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        word_list = [set(word) for word in words]
        ans = 0
        for i in range(len(words)-1):
            for j in range(i+1, len(words)):
                if not word_list[i].intersection(word_list[j]):
                    # print(word_list[i], word_list[j], word_list[i].intersection(word_list[j]))
                    ans = max(len(words[i])*len(words[j]), ans)    
        return ans

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        d = {}
        for word in words:
            mask = 0
            for c in set(word):
                mask |= (1<<(ord(c)-97))
            d[mask] = max(d.get(mask, 0), len(word))
            
        ans = 0
        for k1, k2 in combinations(d.keys(), 2):
            if not k1 & k2:
                ans = max(ans, d[k1]*d[k2])
                
        return ans