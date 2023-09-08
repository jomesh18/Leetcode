'''
118. Pascal's Triangle
Easy

11297

363

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
        ret = [[1]]
        for i in range(1, numRows):
            curr = [1]
            for j in range(1, len(ret[-1])):
                curr.append(ret[-1][j-1]+ret[-1][j])
            curr.append(1)
            ret.append(curr)
        return ret