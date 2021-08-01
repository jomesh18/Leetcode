'''
Pascal's Triangle
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
    def generate(self, numRows: int) -> [[int]]:
        if numRows ==  1: return [[1]]
        res = [[1]]
        for _ in range(2, numRows+1):
        	temp = [1]
        	for i in range(1, len(res[-1])):
        		temp.append(res[-1][i]+res[-1][i-1])
        	temp.append(1)
        	res.append(temp)
        return res

numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

# numRows = 1
# Output: [[1]]

s = Solution()
print(s.generate(numRows))
