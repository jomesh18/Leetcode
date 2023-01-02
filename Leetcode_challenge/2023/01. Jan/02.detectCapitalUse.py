'''
520. Detect Capital
Easy

2424

409

Add to List

Share
We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".
Given a string word, return true if the usage of capitals in it is right.

 

Example 1:

Input: word = "USA"
Output: true
Example 2:

Input: word = "FlaG"
Output: false
 

Constraints:

1 <= word.length <= 100
word consists of lowercase and uppercase English letters.
'''
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        caps = 0
        for i in range(1, len(word)):
            if word[i].isupper():
                caps += 1
        return (caps == len(word)-1 and word[0].isupper()) or caps == 0


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        caps = sum(1 for i in range(1, len(word)) if word[i].isupper())
        return (caps == len(word)-1 and word[0].isupper()) or caps == 0