'''
17. Letter Combinations of a Phone Number
Medium

9671

667

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
1,157,173
Submissions
2,160,794
'''
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        d = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        n = len(digits)
        res = []
        
        def backtrack(i, s):
            if i == n:
                res.append(s)
                return
            for c in d[digits[i]]:
                backtrack(i+1, s+c)
            
        backtrack(0, "")
        return res