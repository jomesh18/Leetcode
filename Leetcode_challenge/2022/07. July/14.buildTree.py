'''
105. Construct Binary Tree from Preorder and Inorder Traversal
Medium

9567

261

Add to List

Share
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

 

Example 1:


Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
Example 2:

Input: preorder = [-1], inorder = [-1]
Output: [-1]
 

Constraints:

1 <= preorder.length <= 3000
inorder.length == preorder.length
-3000 <= preorder[i], inorder[i] <= 3000
preorder and inorder consist of unique values.
Each value of inorder also appears in preorder.
preorder is guaranteed to be the preorder traversal of the tree.
inorder is guaranteed to be the inorder traversal of the tree.
Accepted
769,496
Submissions
1,304,075
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        in_hash = {val: i for i, val in enumerate(inorder)}
        pre_index = 0
        def helper(left, right):
            nonlocal pre_index
            if left > right: return None
            root = TreeNode(preorder[pre_index])
            pre_index += 1
            root.left = helper(left, in_hash[root.val]-1)
            root.right = helper(in_hash[root.val]+1, right)
            return root
        return helper(0, len(preorder)-1)