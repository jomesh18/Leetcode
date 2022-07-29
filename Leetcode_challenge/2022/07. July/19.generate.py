'''
118. Pascal's Triangle
Easy

7189

236

Add to List

Share
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]
 

Constraints:

1 <= numRows <= 30
'''
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        if numRows == 1: return res
        for _ in range(numRows-1):
            t = [1]
            prev = res[-1]
            for i in range(len(prev)-1):
                t.append(prev[i]+prev[i+1])
            t.append(1)
            res.append(t)
        return res