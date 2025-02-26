'''
889. Construct Binary Tree from Preorder and Postorder Traversal
Solved
Medium
Topics
Companies
Given two integer arrays, preorder and postorder where preorder is the preorder traversal of a binary tree of distinct values and postorder is the postorder traversal of the same tree, reconstruct and return the binary tree.

If there exist multiple answers, you can return any of them.

 

Example 1:


Input: preorder = [1,2,4,5,3,6,7], postorder = [4,5,2,6,7,3,1]
Output: [1,2,3,4,5,6,7]
Example 2:

Input: preorder = [1], postorder = [1]
Output: [1]
 

Constraints:

1 <= preorder.length <= 30
1 <= preorder[i] <= preorder.length
All the values of preorder are unique.
postorder.length == preorder.length
1 <= postorder[i] <= postorder.length
All the values of postorder are unique.
It is guaranteed that preorder and postorder are the preorder traversal and postorder traversal of the same binary tree.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        def helper(pre, post):
            if not pre: return None
            if len(pre) == 1: return TreeNode(pre[0])

            root = TreeNode(pre[0])
            left = pre[1]
            
            i = 0
            while i < len(post):
                if post[i] == left:
                    break
                i += 1
            left_post = post[:i+1]
            left_pre = [i for i in pre if i in left_post]
            right_post = post[i+1: -1]
            right_pre = [i for i in pre if i in right_post]
            # print(left_pre, left_post)
            # print(right_pre, right_post)
            root.left = helper(left_pre, left_post)
            root.right = helper(right_pre, right_post)
            return root

        return helper(preorder, postorder)
        