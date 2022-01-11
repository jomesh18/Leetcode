'''
1008. Construct Binary Search Tree from Preorder Traversal
Medium

Given an array of integers preorder, which represents the preorder traversal of a BST (i.e., binary search tree), construct the tree and return its root.

It is guaranteed that there is always possible to find a binary search tree with the given requirements for the given test cases.

A binary search tree is a binary tree where for every node, any descendant of Node.left has a value strictly less than Node.val, and any descendant of Node.right has a value strictly greater than Node.val.

A preorder traversal of a binary tree displays the value of the node first, then traverses Node.left, then traverses Node.right.

 

Example 1:

Input: preorder = [8,5,1,7,10,12]
Output: [8,5,10,1,7,null,12]

Example 2:

Input: preorder = [1,3]
Output: [1,null,3]

 

Constraints:

    1 <= preorder.length <= 100
    1 <= preorder[i] <= 108
    All the values of preorder are unique.

'''
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# class Solution:
#     def bstFromPreorder(self, preorder: [int]):
#         root = TreeNode(preorder[0])
#         stack = [root]
#         i = 1
#         while i < len(preorder):
#             curr = stack.pop()
#             if curr.val > preorder[i]:
#                 curr.left = TreeNode(preorder[i])
#                 i += 1
#                 stack.extend([curr, curr.left])
#             else:
#                 previous = curr
#                 while curr.val < preorder[i] and stack:
#                     previous = curr
#                     curr = stack.pop()
#                 if curr.val < preorder[i]:
#                     previous = curr
#                 previous.right = TreeNode(preorder[i])
#                 i += 1
#                 if previous != curr:
#                     stack.append(curr)
#                 stack.append(previous.right)
#         return root

#from leetcode, fastest
class Solution:
    def bstFromPreorder(self, preorder: [int]):
        iterator = iter(preorder)
        root = current = TreeNode(next(iterator))
        for val in iterator:
            node = TreeNode(val)
            if node.val < current.val:
                node.right = current
                current.left = current = node
            else:
                while current.right is not None and node.val > current.right.val:
                    current.right, current = None, current.right

                node.right = current.right
                current.right = current = node

        while current.right is not None:
            current.right, current = None, current.right

        return root

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

preorder = [8,5,1,7,10,12]
# Output: [8,5,10,1,7,null,12]

preorder = [1,3]
# # Output: [1,null,3]

sol = Solution()
start = sol.bstFromPreorder(preorder)
print(print_tree(start))
