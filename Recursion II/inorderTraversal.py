'''
Binary Tree Inorder Traversal

Given the root of a binary tree, return the inorder traversal of its nodes' values.

 

Example 1:

Input: root = [1,null,2,3]
Output: [1,3,2]

Example 2:

Input: root = []
Output: []

Example 3:

Input: root = [1]
Output: [1]

Example 4:

Input: root = [1,2]
Output: [2,1]

Example 5:

Input: root = [1,null,2]
Output: [1,2]

 

Constraints:

    The number of nodes in the tree is in the range [0, 100].
    -100 <= Node.val <= 100

 
Follow up: Recursive solution is trivial, could you do it iteratively?
'''
# Definition for a binary tree node.

from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
#recursive
# class Solution:
#     def inorderTraversal(self, root) -> [int]:
#         return self.inorderTraversal(root.left)+[root.val]+self.inorderTraversal(root.right) if root else []

#iterative
class Solution:
    def inorderTraversal(self, root) -> [int]:
        if not root: return root
        res, stack = [], []
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right
        return res

def build_tree(root):
    if not root: return root
    start = TreeNode(root[0])
    deq = deque([start])
    i = 1
    while i < len(root):
        curr = deq.popleft()
        if curr:
            curr.left = TreeNode(root[i]) if root[i] is not None else None
            i += 1
            deq.append(curr.left)
            if i < len(root):
                curr.right = TreeNode(root[i]) if root[i] is not None else None
                i += 1
                deq.append(curr.right)
    return start

def print_tree(start):
    res = []
    deq = deque([start])
    while any(deq):
        curr = deq.popleft()
        if curr:
            res.append(curr.val)
            deq.extend([curr.left, curr.right])
        else:
            res.append(None)
    return res

null = None

root = [1,null,2,3]
# Output: [1,3,2]

# root = []
# Output: []

# root = [1]
# Output: [1]

# root = [1,2]
# Output: [2,1]

# root = [1,null,2]
# Output: [1,2]

start = build_tree(root)
print(print_tree(start))

sol = Solution()
print(sol.inorderTraversal(start))
