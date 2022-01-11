'''
404. Sum of Left Leaves
Easy

Given the root of a binary tree, return the sum of all left leaves.

 

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: 24
Explanation: There are two left leaves in the binary tree, with values 9 and 15 respectively.

Example 2:

Input: root = [1]
Output: 0
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#my try
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.sum = 0
        def dfs(node, isleft):
            if not node: return
            if not node.left and not node.right and isleft:
                self.sum += node.val
            dfs(node.left, True)
            dfs(node.right, False)
        dfs(root, False)
        return self.sum

#from leetcode
class Solution(object):
    def sumOfLeftLeaves(self, root):
        if not root: return 0 #base case => node is none
        if root.left and not root.left.left and not root.left.right:
            return root.left.val + self.sumOfLeftLeaves(root.right) #left child is leaf
        return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)   # isn't leaf
