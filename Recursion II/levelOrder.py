'''
Binary Tree Level Order Traversal

Solution
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000
'''
# Definition for a binary tree node.
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#iterative
# class Solution:
#     def levelOrder(self, root) -> [[int]]:
#         if not root: return root
#         q, temp, res = deque([root]), [], [[root.val]]
#         while q:
#             while q:
#                 curr = q.popleft()
#                 if curr:
#                     temp.extend([curr.left, curr.right])
#             if any(temp):
#                 res += [n.val for n in temp if n],
#             q, temp = deque(temp), []
#         return res

#from leetcode, list comprehension
# class Solution:
#     def levelOrder(self, root):
#         ans, level = [], [root]
#         while root and level:
#             ans.append([node.val for node in level])            
#             level = [kid for n in level for kid in (n.left, n.right) if kid]
#         return ans

#from leetcode, recursive dfs
class Solution(object):
    def levelOrder(self, root):
        result = []
        self.helper(root, 0, result)
        return result
    
    def helper(self, root, level, result):
        if not root:
            return
        if len(result) <= level:
            result.append([])
        result[level].append(root.val)
        self.helper(root.left, level+1, result)
        self.helper(root.right, level+1, result)

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

root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]

root = [1]
# # Output: [[1]]

root = []
# # Output: []

start = build_tree(root)
print(print_tree(start))

sol = Solution()
print(sol.levelOrder(start))
