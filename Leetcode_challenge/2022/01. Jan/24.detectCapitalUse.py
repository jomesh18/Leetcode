'''
520. Detect Capital
Easy

1263

338

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
Accepted
229,530
Submissions
416,491
'''
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        first_capital, capital_count, lower_count = False, 0, 0
        
        for c in word:
            if c.islower(): lower_count += 1
            else: capital_count += 1

        if word[0].isupper(): first_capital = True

        if capital_count == len(word) or first_capital and lower_count == len(word)-1 or lower_count == len(word):
            return True
        return False


#same as above
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        capital_count = 0
        
        for c in word:
            if c.isupper(): capital_count += 1

        return  capital_count == len(word) or (word[0].isupper() and capital_count == 1) or capital_count == 0: