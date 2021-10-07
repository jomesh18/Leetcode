'''
Validate Binary Search Tree

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
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root) -> bool:
        def helper(root, low, high):
            if not root: return True
            if root.val <= low or root.val >= high: return False
            return helper(root.left, low, root.val) and helper(root.right, root.val, high)
        return helper(root, float("-inf"), float("inf"))

def buildTree(root):
    if not root: return None
    tree = TreeNode(root[0])
    q = deque([tree])
    i = 1
    while i < len(root):
        curr = q.popleft()
        if curr:
            curr.left = TreeNode(root[i]) if root[i] is not None else None
            q.append(curr.left)
            i += 1
            if i < len(root):
                curr.right = TreeNode(root[i]) if root[i] is not None else None
                q.append(curr.right)
                i += 1
    return tree

def print_tree(tree):
    res = []
    q = deque([tree])
    while any(q):
        curr = q.popleft()
        if curr:
            res.append(curr.val)
            q.extend([curr.left, curr.right])
        else:
            res.append(None)
    return res

null = None
true = True
false = False

root = [2,1,3]
# # Output: true

# root = [5,1,4,null,null,3,6]
# # Output: false

# root = [5,1,6,null,null,3,7]
# Output: False

# root = [5, 1, 7, null, null, 6, 8]
# # Output: True

# root = [1,1]
# # Output: False

tree = buildTree(root)
print(print_tree(tree))
sol = Solution()
print(sol.isValidBST(tree))
