'''
226. Invert Binary Tree
Easy

Given the root of a binary tree, invert the tree, and return its root.

 

Example 1:

Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

Example 2:

Input: root = [2,1,3]
Output: [2,3,1]

Example 3:

Input: root = []
Output: []

 

Constraints:

    The number of nodes in the tree is in the range [0, 100].
    -100 <= Node.val <= 100

'''
# Definition for a binary tree node.
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root):
        if not root: return root
        root.right, root.left = self.invertTree(root.left), self.invertTree(root.right)
        return root

def build_tree(root):
    if not root: return root
    start = TreeNode(root[0])
    q = deque([start])
    i = 1
    while i < len(root):
        curr = q.popleft()
        if curr:
            curr.left = TreeNode(root[i]) if root[i] is not None else None
            q.append(curr.left)
            i += 1
            if i < len(root):
                curr.right = TreeNode(root[i]) if root[i] is not None else None
                i += 1
                q.append(curr.right)
    return start

def print_tree(start):
    if not start: return start
    q = deque([start])
    res = []
    while any(q):
        curr = q.popleft()
        if curr:
            res.append(curr.val)
            q.extend([curr.left, curr.right])
        else:
            res.append(None)
    return res

root = [4,2,7,1,3,6,9]
# Output: [4,7,2,9,6,3,1]

# root = [2,1,3]
# # Output: [2,3,1]

# root = []
# Output: []

start = build_tree(root)
print(print_tree(start))

sol = Solution()
print(print_tree(sol.invertTree(start)))
