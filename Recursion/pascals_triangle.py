'''
Pascal's Triangle II

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
#without memoization
# class Solution:
#     def getRow(self, rowIndex: int) -> [int]:
#         res = []
#         for j in range(rowIndex+1):
#             res.append(self.f(rowIndex, j))
#         return res

#     def f(self, i, j):
#         if j == 0 or j == i:
#             return 1
#         return self.f(i-1, j-1) + self.f(i-1, j)

#too slow, so used memoization
class Solution:
    def getRow(self, rowIndex: int) -> [int]:
        cache = {}
        def f(i, j):
            if (i, j) in cache: return cache[(i, j)]
            if j == 0 or j == i: return 1
            elem = f(i-1, j-1) + f(i-1, j)
            cache[(i, j)] = elem
            return elem
        return [f(rowIndex, j) for j in range(rowIndex+1)]

#from leetcode, recursive
def pascalRecursive(i):
    if i == 0:
        return [1]
    if i == 1:
        return [1,1]
    
    prevRow = pascal(i-1)
    newRow = [1 for i in range(len(prevRow)+1)]
    
    for i in range(1,len(prevRow)):
        newRow[i] = prevRow[i-1] + prevRow[i]
    
    return newRow

#from leetcode, iterative, using zip
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row = [1]
        for _ in range(rowIndex):
            row = [x + y for x, y in zip([0]+row, row+[0])]
        return row
#from leetcode, same as above
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1]
        for _ in range(rowIndex):
            res = [1] + [a+b for a, b in zip(res, res[1:])] + [1]
        return res

rowIndex = 3
rowIndex = 33
# Output: [1,3,3,1]
s = Solution()
print(s.getRow(rowIndex))
