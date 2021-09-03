'''
Unique Binary Search Trees II

Given an integer n, return all the structurally unique BST's (binary search trees), which has exactly n nodes of unique values from 1 to n. Return the answer in any order.

 

Example 1:

Input: n = 3
Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]

Example 2:

Input: n = 1
Output: [[1]]

 

Constraints:

    1 <= n <= 8

'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def generateTrees(self, n: int) -> [TreeNode]:

        if n == 0:

            return [[]]

        return self.dfs(1, n+1)        

    def dfs(self, start, end):

        if start == end:

            return None

        result = []

        for i in range(start, end):

            for l in self.dfs(start, i) or [None]:

                for r in self.dfs(i+1, end) or [None]:

                    node = TreeNode(i)

                    node.left, node.right  = l, r

                    result.append(node)

        return result