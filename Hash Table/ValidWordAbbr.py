'''
648 · Unique Word Abbreviation
Algorithms
Medium
Accepted Rate33%
Description
Solution
Notes
Discuss
Leaderboard
Description

An abbreviation of a word follows the form <first letter><number><last letter>. Below are some examples of word abbreviations:

a) it                      --> it    (no abbreviation)



     1

b) d|o|g                   --> d1g



              1    1  1

     1---5----0----5--8

c) i|nternationalizatio|n  --> i18n



              1

     1---5----0

d) l|ocalizatio|n          --> l10n

Assume you have a dictionary and given a word, find whether its abbreviation is unique in the dictionary. A word's abbreviation is unique if no other word from the dictionary has the same abbreviation.
Example

Example1

Input:

[ "deer", "door", "cake", "card" ]

isUnique("dear")

isUnique("cart")

Output:

false

true

Explanation:

Dictionary's abbreviation is ["d2r", "d2r", "c2e", "c2d"].

"dear" 's abbreviation is "d2r" , in dictionary.

"cart" 's abbreviation is "c2t" , not in dictionary.

Example2

Input:

[ "deer", "door", "cake", "card" ]

isUnique("cane")

isUnique("make")

Output:

false

true

Explanation:

Dictionary's abbreviation is ["d2r", "d2r", "c2e", "c2d"].

"cane" 's abbreviation is "c2e" , in dictionary.

"make" 's abbreviation is "m2e" , not in dictionary.
'''
# from collections import defaultdict
# class ValidWordAbbr:
#     """
#     @param: dictionary: a list of words
#     """
#     def __init__(self, dictionary):
#         # do intialization if necessary
#         self.d = defaultdict(list)
#         for word in dictionary:
#             abb = self.find_abb(word)
#             self.d[abb].append(word)
#     """
#     @param: word: a string
#     @return: true if its abbreviation is unique or false
#     """
#     def isUnique(self, word):
#         # write your code here
#         abb = self.find_abb(word)
#         if abb in self.d and len(self.d[abb]) == 1 and self.d[abb][0] == word:
#             return True
#         if abb not in self.d:
#             return True
#         return False

#     def find_abb(self, word):
#         if len(word)< 2:
#             abb = word
#         else:
#             abb = word[0]+str(len(word)-2)+word[-1]
#         return abb

#lintcode, highlight
class ValidWordAbbr:
    
    def __init__(self, dictionary):
        # do intialization if necessary
        self.map = {}
        for word in dictionary:
            abbr = self.word_to_abbr(word)
            if abbr not in self.map:
                self.map[abbr] = set() 
            self.map[abbr].add(word)

    def word_to_abbr(self, word):
        if len(word) <= 1:
            return word
        return word[0] + str(len(word[1:-1])) + word[-1]
        
    def isUnique(self, word):
        # write your code here
        abbr = self.word_to_abbr(word)
        if abbr not in self.map:
            return True
        for word_in_dict in self.map[abbr]:
            if word != word_in_dict:
                return False
        return True

# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param = obj.isUnique(word)