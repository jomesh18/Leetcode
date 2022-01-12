'''
Validate Binary Search Tree

Solution
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:


Input: root = [2,1,3]
Output: true
Example 2:


Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
 

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

#recursive
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(node, ma, mi):
            if node.val<=mi or node.val>=ma:
                return False
            if node.left:
                lef = helper(node.left, node.val, mi)
                if not lef: return False
            if node.right:
                rig = helper(node.right, ma, node.val)
                if not rig: return False
            return True
        return helper(root, float("inf"), float("-inf"))

#iterative
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = [(root, float('-inf'), float('inf'))]
        while stack:
            node, lower, upper = stack.pop()
            if lower >= node.val or node.val >= upper:
                return False

            if node.left:
                stack.append([node.left, lower, node.val])
            if node.right:
                stack.append([node.right, node.val, upper])

        return True

#concise recursive
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        def validate(node, lower=float("-inf"), upper=float("inf")):
            if not node: return True
            
            if node.val <= lower or node.val >= upper: return False

            return validate(node.left, lower, node.val) and validate(node.right, node.val, upper)

# inorder traversal recursive
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def inorder(root):
            if not root: return True
            if not inorder(root.left):
                return False
            if root.val <= self.prev:
                return False
            self.prev = root.val
            return inorder(root.right)

        self.prev = float("-inf")
        return inorder(root)

# iteratvie inorder traversal
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        stack, prev = [], float("-inf")

        while stack or root:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            if root.val <= prev.val: return False
            prev = root.val
            root = root.right
        return True
