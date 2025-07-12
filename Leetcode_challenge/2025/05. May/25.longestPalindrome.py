'''
2131. Longest Palindrome by Concatenating Two Letter Words
Solved
Medium
Topics
premium lock icon
Companies
Hint
You are given an array of strings words. Each element of words consists of two lowercase English letters.

Create the longest possible palindrome by selecting some elements from words and concatenating them in any order. Each element can be selected at most once.

Return the length of the longest palindrome that you can create. If it is impossible to create any palindrome, return 0.

A palindrome is a string that reads the same forward and backward.

 

Example 1:

Input: words = ["lc","cl","gg"]
Output: 6
Explanation: One longest palindrome is "lc" + "gg" + "cl" = "lcggcl", of length 6.
Note that "clgglc" is another longest palindrome that can be created.
Example 2:

Input: words = ["ab","ty","yt","lc","cl","ab"]
Output: 8
Explanation: One longest palindrome is "ty" + "lc" + "cl" + "yt" = "tylcclyt", of length 8.
Note that "lcyttycl" is another longest palindrome that can be created.
Example 3:

Input: words = ["cc","ll","xx"]
Output: 2
Explanation: One longest palindrome is "cc", of length 2.
Note that "ll" is another longest palindrome that can be created, and so is "xx".
 

Constraints:

1 <= words.length <= 105
words[i].length == 2
words[i] consists of lowercase English letters.
'''
class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        word_dict = Counter(words)
        ans = 0
        unpaired = False
        # print(word_dict)
        for word in word_dict:
            rev_word = word[::-1]
            if rev_word == word:
                count = word_dict[word]
                if count & 1:
                    unpaired = True
                    count -= 1
                ans += count*2
                continue
            if rev_word in word_dict:
                count = min(word_dict[word], word_dict[rev_word])
                word_dict[word] -= count
                word_dict[rev_word] -= count
                ans += count*4
        return ans+2 if unpaired else ans
