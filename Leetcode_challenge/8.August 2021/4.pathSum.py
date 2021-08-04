'''
Path Sum II

Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where each path's sum equals targetSum.

A leaf is a node with no children.

 

Example 1:

Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: [[5,4,11,2],[5,8,4,5]]

Example 2:

Input: root = [1,2,3], targetSum = 5
Output: []

Example 3:

Input: root = [1,2], targetSum = 0
Output: []

 

Constraints:

    The number of nodes in the tree is in the range [0, 5000].
    -1000 <= Node.val <= 1000
    -1000 <= targetSum <= 1000

'''

# Definition for a binary tree node.
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> [[int]]:
        if not root: return []
        res = []
        def dfs(node, temp, s):
            # print(temp, s)
            # if node: print(node.val)
            if not node: return
            if not node.left and not node.right:
                if s+node.val == targetSum:
                    res.append(temp[:]+[node.val])
                return
            temp.append(node.val)
            s += node.val
            dfs(node.left, temp, s)
            dfs(node.right, temp, s)
            temp.remove(node.val)
            s -= node.val
        dfs(root, [], 0)
        return res

def build_tree(root):
    if not root: return []
    start = TreeNode(root[0])
    q = deque([start])
    i = 1
    while i<len(root):
        curr = q.popleft()
        if curr:
            curr.left = TreeNode(root[i]) if root[i] is not None else None
            q.append(curr.left)
            i += 1
            if i < len(root):
                curr.right = TreeNode(root[i]) if root[i] is not None else None
                q.append(curr.right)
            i += 1
    return start

def print_tree(start):
    if not start: return []
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

root = [5,4,8,11,null,13,4,7,2,null,null,5,1]
targetSum = 22
# Output: [[5,4,11,2],[5,8,4,5]]

# root = [1,2,3]
# targetSum = 5
# # Output: []

# root = [1,2]
# targetSum = 0
# # Output: []

# root = [1,-2,-3,1,3,-2,null,-1]
# targetSum = 2
# Output: [[1,-2,3]]

start = build_tree(root)
print(print_tree(start))

sol = Solution()
print(sol.pathSum(start, targetSum))
