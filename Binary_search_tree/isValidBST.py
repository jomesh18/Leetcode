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

# class Solution:
#     def isValidBST(self, root: TreeNode) -> bool:
#         def dfs(root):
#             return dfs(root.left)+[root.val]+dfs(root.right) if root else []
#         res = dfs(root)
#         # print(res)
#         return len([res[i] for i in range(1, len(res)) if res[i]<=res[i-1]])==0

#Recursive Traversal with Valid Range
# class Solution:
#     def isValidBST(self, root: TreeNode) -> bool:
#         def validate(root, lower, upper):
#             if not root: return True
#             if root.val<=lower or root.val>=upper:
#                 return False
#             return validate(root.left, lower, root.val) and validate(root.right, root.val, upper)
#         return validate(root, float("-inf"), float("inf"))

#Iterative Traversal with Valid Range
# class Solution:
#     def isValidBST(self, root: TreeNode) -> bool:
#         if not root:
#             return True
#         stack = [(root, float("-inf"), float("inf"))]
#         while stack:
#             curr, lower, upper = stack.pop()
#             if not curr:
#                 continue
#             val = root.val
#             if val<=lower or val>=upper:
#                 return False
#             stack.append((root.right, val, upper))
#             stack.append((root.left, lower, val))
#         return True

#Recursive Inorder Traversal
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        def inorder(root):
            if not root:
                return True
            if not inorder(root.left):
                return False
            if root.val <= self.prev:
                return False
            self.prev = root.val
            return inorder(root.right)

        self.prev = -math.inf
        return inorder(root)
#Iterative Inorder Traversal
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        stack, prev = [], float("-inf")

        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            # If next element in inorder traversal
            # is smaller than the previous one
            # that's not BST.
            if root.val <= prev:
                return False
            prev = root.val
            root = root.right

        return True
def build_tree(root):
    start = TreeNode(root[0])
    curr = start
    i = 1
    q = deque([start])
    while i<len(root):
        curr = q.popleft()
        if curr:
            curr.left = TreeNode(root[i]) if root[i] is not None else None
            q.append(curr.left)
            i += 1
            if i<len(root):
                curr.right = TreeNode(root[i]) if root[i] is not None else None
                q.append(curr.right)
        i += 1
    return start

def print_tree(start):
    res = []
    q = deque([start])
    while any(q):
        curr = q.popleft()
        if curr:
            res.append(curr.val)
            q.extend([curr.left, curr.right])
        else:
            res.append(None)
    return res

null = None

# root = [2,1,3]
# Output: true

# root = [5,1,4,null,null,3,6]
# # Output: false

root = [5,4,6,null,null,3,7]
# Output: false

# root = [2,2,2]
# # Output: false

start = build_tree(root)
print(print_tree(start))
s = Solution()
print(s.isValidBST(start))
