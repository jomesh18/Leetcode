'''
Binary Tree Inorder Traversal

Solution
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

# class Solution:
#     def inorderTraversal(self, root: TreeNode) -> [int]:
#         res = []
#         def dfs(root):
#             if not root: return root     
#             dfs(root.left)
#             res.append(root.val)
#             dfs(root.right)
#         dfs(root)
#         return res

# using recursion
# class Solution:
#     def inorderTraversal(self, root: TreeNode) -> [int]:
#         return self.inorderTraversal(root.left)+[root.val]+self.inorderTraversal(root.right) if root else []

# using iteration, dfs
class Solution:
    def inorderTraversal(self, root: TreeNode) -> [int]:
        res, stack = [], []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return res
            node = stack.pop()
            res.append(node.val)
            root = node.right

def create_tree(l):
    if not l: return l
    if l[0] is not None: start = TreeNode(l[0])
    q = deque([start])
    i = 1
    while i < len(l):
        current = q.popleft()
        if current:
            if l[i] is not None:
                current.left = TreeNode(l[i])
                q.append(current.left)
            i += 1
            if i < len(l) and l[i] is not None:
                current.right = TreeNode(l[i])
                q.append(current.right)
            i += 1
    return start

def print_tree(start):
    if not start: return start
    q = deque([start])
    res = []
    while any(q):
        current = q.popleft()
        if current:
            res.append(current.val)
            q.extend([current.left, current.right])
        else:
            res.append(current)
    print(res)

null = None
root = [1,null,2,3]
Output = [1,3,2]

start = create_tree(root)
print_tree(start)
s = Solution()
ans = s.inorderTraversal(start)
print(ans)
print(Output == ans)
