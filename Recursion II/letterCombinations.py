'''
Letter Combinations of a Phone Number

Solution
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
'''
class Solution:
    def letterCombinations(self, digits: str) -> [str]:
        if not digits: return []
        mappings = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        res = []
        def backtrack(temp, pos):
            if pos == len(digits):
                res.append("".join(temp))
                return
            d = digits[pos]
            chars = mappings[d]
            for c in chars:
                backtrack(temp+[c], pos+1)
        backtrack([], 0)
        return res

digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

digits = ""
# Output: []

# digits = "2"
# Output: ["a","b","c"]

# digits = "234"
# # Output: 

sol = Solution()
print(sol.letterCombinations(digits))
