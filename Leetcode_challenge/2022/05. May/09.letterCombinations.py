'''
17. Letter Combinations of a Phone Number
Medium

10059

680

Add to List

Share
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.



 

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]
 

Constraints:

0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].
Accepted
1,184,195
Submissions
2,197,660
'''
#recursive
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        if not digits: return []
        res = []
        
        def dfs(i, s):
            if i == len(digits):
                res.append(s)
                return
            for c in d[digits[i]]:
                dfs(i+1, s+c)
            
        dfs(0, '')
        return res

#iterative
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        if not digits: return []
        res = ['']
        for i in range(len(digits)):
            res = [prev+l for prev in res for l in d[digits[i]]]
        return res