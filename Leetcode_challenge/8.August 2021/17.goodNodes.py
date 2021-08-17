'''
Count Good Nodes in Binary Tree

Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.

 

Example 1:

Input: root = [3,1,4,3,null,1,5]
Output: 4
Explanation: Nodes in blue are good.
Root Node (3) is always a good node.
Node 4 -> (3,4) is the maximum value in the path starting from the root.
Node 5 -> (3,4,5) is the maximum value in the path
Node 3 -> (3,1,3) is the maximum value in the path.

Example 2:

Input: root = [3,3,null,4,2]
Output: 3
Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.

Example 3:

Input: root = [1]
Output: 1
Explanation: Root is considered as good.

 

Constraints:

    The number of nodes in the binary tree is in the range [1, 10^5].
    Each node's value is between [-10^4, 10^4].
'''
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        def dfs(node, maximum):
            if not node: return
            if node.val >= maximum:
                maximum = node.val
                self.count += 1
            dfs(node.left, maximum)
            dfs(node.right, maximum)

        dfs(root, float("-inf"))
        return self.count

def build_tree(root):
    if not root: return []
    start = TreeNode(root[0])
    q = deque([start])
    i = 1
    while i < len(root):
        curr = q.popleft()
        if curr:
            curr.left = TreeNode(root[i]) if root[i] is not None else None
            i += 1
            if i < len(root):
                curr.right = TreeNode(root[i]) if root[i] is not None else None
            q.extend([curr.left, curr.right])
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

root = [3,1,4,3,null,1,5]
# Output: 4

# root = [3,3,null,4,2]
# # # Output: 3

# root = [1]
# # Output: 1

start = build_tree(root)
print(print_tree(start))

sol = Solution()
print(sol.goodNodes(start))
