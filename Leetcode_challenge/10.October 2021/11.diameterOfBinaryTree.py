'''
543. Diameter of Binary Tree
Easy

Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

 

Example 1:

Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

Example 2:

Input: root = [1,2]
Output: 1

 

Constraints:

    The number of nodes in the tree is in the range [1, 104].
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
    def diameterOfBinaryTree(self, root) -> int:
        self.res = 0
        def helper(node):
            if not node: return 0
            left = helper(node.left)
            right = helper(node.right)
            self.res = max(self.res, left + right)
            return 1+max(left, right)
        helper(root)
        return self.res
        
def create_tree(root):
    if not root: return root
    start = TreeNode(root[0])
    q = deque([start])
    i = 1
    while i < len(root):
        curr = q.popleft()
        if curr:
            curr.left = TreeNode(root[i]) if root[i] is not None else None
            i += 1
            q.append(curr.left)
            if i < len(root):
                curr.right = TreeNode(root[i]) if root[i] is not None else None
                i += 1
                q.append(curr.right)
    return start

root = [1,2,3,4,5]
# Output: 3

# root = [1,2]
# # Output: 1

start = create_tree(root)

sol = Solution()
print(sol.diameterOfBinaryTree(start))
