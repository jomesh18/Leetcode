'''
Balanced Binary Tree

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

    a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

 

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: true

Example 2:

Input: root = [1,2,2,3,3,null,null,4,4]
Output: false

Example 3:

Input: root = []
Output: true

 

Constraints:

    The number of nodes in the tree is in the range [0, 5000].
    -104 <= Node.val <= 104

'''

# Definition for a binary tree node.
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def get_height(node, l_h, r_h):
            if not node: return 0
            l_h = get_height(node.left, l_h+1, r_h)
            r_h = get_height(node.right, l_h, r_h+1)
            if abs(l_h - r_h) > 1:
                return False

        return get_height(root, 0, 0)


def build_tree(root):
    if not root: return None
    start = TreeNode(root[0])
    q = deque([start])
    i = 1
    while i<len(root):
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

null = None

# root = [3,9,20,null,null,15,7]
# Output: true

root = [1,2,2,3,3,null,null,4,4]
# # Output: false

# root = []
# Output: true

start = build_tree(root)
print(print_tree(start))

sol = Solution()
print(sol.isBalanced(start))
