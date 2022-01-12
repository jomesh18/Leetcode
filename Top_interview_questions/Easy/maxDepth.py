'''
 Maximum Depth of Binary Tree

Solution
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2
 

Constraints:

The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#accepted
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.max_len = 0
        def dfs(node, depth):
            if not node: return
            if not node.left and not node.right:
                self.max_len = max(self.max_len, depth+1)
            dfs(node.left, depth+1)
            dfs(node.right, depth+1)
            
        dfs(root, 0)
        return self.max_len

#simple, from leetcode
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1