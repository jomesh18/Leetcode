'''
993. Cousins in Binary Tree
Easy

Given the root of a binary tree with unique values and the values of two different nodes of the tree x and y, return true if the nodes corresponding to the values x and y in the tree are cousins, or false otherwise.

Two nodes of a binary tree are cousins if they have the same depth with different parents.

Note that in a binary tree, the root node is at the depth 0, and children of each depth k node are at the depth k + 1.

 

Example 1:

Input: root = [1,2,3,4], x = 4, y = 3
Output: false

Example 2:

Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
Output: true

Example 3:

Input: root = [1,2,3,null,4], x = 2, y = 3
Output: false

 

Constraints:

    The number of nodes in the tree is in the range [2, 100].
    1 <= Node.val <= 100
    Each node has a unique value.
    x != y
    x and y are exist in the tree.

'''
# Definition for a binary tree node.
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#using dfs
class Solution:
    def isCousins(self, root, x: int, y: int) -> bool:
        res = []
        def dfs(node, parent, depth, found_both):
            if found_both == 2: return
            if not node: return
            if node.val == x or node.val == y:
                res.append((node.val, depth, parent.val if parent else None))
                found_both += 1
            for n in (node.left, node.right):
                dfs(n, node, depth+1, found_both)
        dfs(root, None, 0, 0)
        # print(res)
        return res[0][-1] != res[1][-1] and res[0][1] == res[1][1]

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

root = [1,2,3,4]
x = 4
y = 3
# Output: false

# root = [1,2,3,null,4,null,5]
# x = 5
# y = 4
# # Output: true

root = [1,2,3,null,4]
x = 2
y = 3
# # Output: false

root = [1,null,2,3,null,null,4,null,5]
x = 1
y = 3


start = build_tree(root)
print(print_tree(start))

sol = Solution()
print(sol.isCousins(start, x, y))
