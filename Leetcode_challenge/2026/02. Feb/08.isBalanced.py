'''
110. Balanced Binary Tree
Solved
Easy
Topics
premium lock icon
Companies
Given a binary tree, determine if it is height-balanced.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: true
Example 2:


Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
Example 3:

Input: root = []
Output: true
 

Constraints:

The number of nodes in the tree is in the range [0, 5000].
-104 <= Node.val <= 104
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        def dfs(node):
            if not node: return (True, 0)
            ls, lv = dfs(node.left)
            rs, rv = dfs(node.right)
            if not ls or not rs or abs(lv - rv) > 1: return (False, 0)
            return (True, 1 + max(lv, rv))
        
        return dfs(root)[0]
