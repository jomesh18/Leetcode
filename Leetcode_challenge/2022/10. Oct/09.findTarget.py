'''
653. Two Sum IV - Input is a BST
Easy

4713

219

Add to List

Share
Given the root of a Binary Search Tree and a target number k, return true if there exist two elements in the BST such that their sum is equal to the given target.

 

Example 1:


Input: root = [5,3,6,2,4,null,7], k = 9
Output: true
Example 2:


Input: root = [5,3,6,2,4,null,7], k = 28
Output: false
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-104 <= Node.val <= 104
root is guaranteed to be a valid binary search tree.
-105 <= k <= 105
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        self.s = set()
        def helper(node):
            if not node: return False
            if k-node.val in self.s: return True
            self.s.add(node.val)
            return helper(node.left) or helper(node.right)
        return helper(root)

#using sorted property of bst inorder traversal
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def inorder(node):
            if node:
                yield from inorder(node.left)
                yield node.val
                yield from inorder(node.right)
            
        def reversed_inorder(node):
            if node:
                yield from reversed_inorder(node.right)
                yield node.val
                yield from reversed_inorder(node.left)
            
        left_gen, right_gen = inorder(root), reversed_inorder(root)
        left, right = next(left_gen), next(right_gen)
        
        while left < right:
            if left+right < k:
                left = next(left_gen)
            elif left+right > k:
                right = next(right_gen)
            else:
                return True
        return False