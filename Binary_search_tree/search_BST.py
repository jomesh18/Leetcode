'''
Search in a Binary Search Tree

You are given the root of a binary search tree (BST) and an integer val.

Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.

 

Example 1:

Input: root = [4,2,7,1,3], val = 2
Output: [2,1,3]

Example 2:

Input: root = [4,2,7,1,3], val = 5
Output: []

 

Constraints:

    The number of nodes in the tree is in the range [1, 5000].
    1 <= Node.val <= 107
    root is a binary search tree.
    1 <= val <= 107

'''

# Definition for a binary tree node.
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#iterative
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        curr = root
        while curr:
            if val > curr.val:
                curr = curr.right
            elif val < curr.val:
                curr = curr.left
            else:
                return curr

#recursive
# class Solution:
#     def searchBST(self, root: TreeNode, val: int) -> TreeNode:
#         if not root:
#             return None
#         if root.val == val:
#             return root
#         elif val > root.val:
#             return self.searchBST(root.right, val)
#         else:
#             return self.searchBST(root.left, val)

#from leetcode
class Solution:
    def searchBST(self, root, val):
        if root and val < root.val: return self.searchBST(root.left, val)
        elif root and val > root.val: return self.searchBST(root.right, val)
        return root

def build_tree(root):
    start = TreeNode(root[0])
    q = deque([start])
    i = 1
    while i < len(root):
        curr = q.popleft()
        if curr:
            curr.left = TreeNode(root[i]) if root[i] is not None else None
            i += 1
            q.append(curr.left)
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

root = [4,2,7,1,3]
val = 2
# Output: [2,1,3]

# root = [4,2,7,1,3]
# val = 5
# Output: []

start = build_tree(root)
print(print_tree(start))

s = Solution()
res = s.searchBST(start, val)
print(print_tree(res))
