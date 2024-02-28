'''
513. Find Bottom Left Tree Value
Medium

3415

272

Add to List

Share
Given the root of a binary tree, return the leftmost value in the last row of the tree.

 

Example 1:


Input: root = [2,1,3]
Output: 1
Example 2:


Input: root = [1,2,3,4,null,5,6,null,null,7]
Output: 7
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        ans = root.val
        max_d = 1
        def dfs(node, d):
            nonlocal ans, max_d
            if not node: return
            if node.left:
                dfs(node.left, d+1)
            else:
                if d > max_d:
                    ans = node.val
                    max_d = d
            if node.right:
                dfs(node.right, d+1)
        dfs(root, 1)
        return ans