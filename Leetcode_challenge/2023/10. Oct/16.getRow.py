'''
119. Pascal's Triangle II
Easy

4611

319

Add to List

Share
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

Example 1:

Input: rowIndex = 3
Output: [1,3,3,1]
Example 2:

Input: rowIndex = 0
Output: [1]
Example 3:

Input: rowIndex = 1
Output: [1,1]
 

Constraints:

0 <= rowIndex <= 33
 

Follow up: Could you optimize your algorithm to use only O(rowIndex) extra space?
'''
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        curr = [1]
        if rowIndex == 0: return curr 
        for _ in range(rowIndex):
            curr = [1]+[curr[i]+curr[i+1] for i in range(len(curr)-1)]+[1]
        return curr