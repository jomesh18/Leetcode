'''
171. Excel Sheet Column Number
Easy

2751

250

Add to List

Share
Given a string columnTitle that represents the column title as appear in an Excel sheet, return its corresponding column number.

For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...
 

Example 1:

Input: columnTitle = "A"
Output: 1
Example 2:

Input: columnTitle = "AB"
Output: 28
Example 3:

Input: columnTitle = "ZY"
Output: 701
 

Constraints:

1 <= columnTitle.length <= 7
columnTitle consists only of uppercase English letters.
columnTitle is in the range ["A", "FXSHRXW"].
Accepted
460,227
Submissions
769,903
'''

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans = 0
        for c in columnTitle:
            ans = ans * 26 + (ord(c)-ord('A')+1)
        return ans
