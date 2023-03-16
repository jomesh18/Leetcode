'''
106. Construct Binary Tree from Inorder and Postorder Traversal
Medium

6225

90

Add to List

Share
Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.

 

Example 1:


Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
Output: [3,9,20,null,null,15,7]
Example 2:

Input: inorder = [-1], postorder = [-1]
Output: [-1]
 

Constraints:

1 <= inorder.length <= 3000
postorder.length == inorder.length
-3000 <= inorder[i], postorder[i] <= 3000
inorder and postorder consist of unique values.
Each value of postorder also appears in inorder.
inorder is guaranteed to be the inorder traversal of the tree.
postorder is guaranteed to be the postorder traversal of the tree.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# O(h*n) where h is the height of the tree, unbalacned tree h = n, O(n*n)
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder: return None
        root = TreeNode(postorder[-1])
        for i in range(len(inorder)):
            if inorder[i] == postorder[-1]:
                pos = i
                break
        pos_left, pos_right = [], []
        in_left, in_right = inorder[:i], inorder[i+1:]
        set_in_left = set(in_left)
        for i in range(len(postorder)-1):
            v = postorder[i]
            if v in set_in_left:
                pos_left.append(v)
            else:
                pos_right.append(v)
        root.left = self.buildTree(in_left, pos_left)
        root.right = self.buildTree(in_right, pos_right)
        return root

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        d = {v: i for i, v in enumerate(inorder)}
        def helper(lo, hi):
            if lo > hi: return None
            root = TreeNode(postorder.pop())
            mid = d[root.val]
            root.right = helper(mid+1, hi)
            root.left = helper(lo, mid-1)
            return root
        return helper(0, len(inorder)-1)