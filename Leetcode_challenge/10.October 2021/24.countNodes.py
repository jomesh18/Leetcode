'''
222. Count Complete Tree Nodes
Medium

3852

289

Add to List

Share
Given the root of a complete binary tree, return the number of the nodes in the tree.

According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Design an algorithm that runs in less than O(n) time complexity.

 

Example 1:


Input: root = [1,2,3,4,5,6]
Output: 6
Example 2:

Input: root = []
Output: 0
Example 3:

Input: root = [1]
Output: 1
 

Constraints:

The number of nodes in the tree is in the range [0, 5 * 104].
0 <= Node.val <= 5 * 104
The tree is guaranteed to be complete.
Accepted
345,734
Submissions
653,968
'''

# Definition for a binary tree node.
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countNodes(self, root) -> int:
        self.height = 0
        self.count = 0
        curr = root
        while curr and curr.left:
            self.height += 1
            curr = curr.left

        # print(self.height)
        def dfs(node, level):
            if not node: return
            if level == self.height:
                # print("node is {}".format(node.val))
                self.count += 1
            
            dfs(node.left, level+1)
            dfs(node.right, level+1)

        dfs(root, 0)
        return (2**self.height)-1+self.count

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

root = [1,2,3,4,5,6]
# Output: 6

root = []
# # Output: 0

root = [1]
# Output: 1

start = build_tree(root)
print(print_tree(start))

sol = Solution()
print(sol.countNodes(start))
