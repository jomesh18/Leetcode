'''
Maximum Depth of N-ary Tree

Given a n-ary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).

 

Example 1:

Input: root = [1,null,3,2,4,null,5,6]
Output: 3

Example 2:

Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: 5

 

Constraints:

    The total number of nodes is in the range [0, 104].
    The depth of the n-ary tree is less than or equal to 1000.

'''

# Definition for a Node.
from collections import deque
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

#dfs, my try
# class Solution:
#     def maxDepth(self, root: 'Node') -> int:
#         ans = float("-inf")
#         def helper(node, d):
#             nonlocal ans
#             if not node: return d-1
#             if node.children:
#                 for n in node.children:
#                     ans = max(ans, helper(n, d+1))
#             return max(ans, d)
#         return helper(root, 1)

# from leetcode, bottom up approach, dfs
class Solution(object):
    def maxDepth(self, root):
        if not root: return 0
        depth = 0
        if root.children:
            for n in root.children:
                depth = max(depth, self.maxDepth(n))
        return depth + 1

# from leetcode, bottom up approach, dfs
# class Solution(object):
#     def maxDepth(self, root):
#         if not root: return 0
#         if not root.children: return 1
#         return max(self.maxDepth(node) for node in root.children) + 1

#from leetcode, bfs:
# class Solution:
#     def maxDepth(self, root):
#         if not root: return 0
#         q = deque([root])
#         depth = 0
#         while q:
#             l = len(q)
#             for i in range(l):
#                 curr = q.popleft()
#                 if curr.children:
#                     q.extend(curr.children)
#             depth += 1
#         return depth

def build_tree(root):
    if not root: return []
    start = Node(root[0])
    i = 2
    q = deque([start])
    while i < len(root):
        curr = q.popleft()
        child_list = []
        while i<len(root) and root[i] is not None:
            child = Node(root[i])
            i += 1
            q.append(child)
            child_list.append(child)
        curr.children = child_list
        i += 1
    return start

def print_tree(start):
    if not start: return []
    res = [start.val, None]
    q = deque([start])
    while any(q):
        curr = q.popleft()
        if curr:
            if curr.children:
                q.extend(curr.children)
                res.extend([node.val for node in curr.children])
            res.append(None)
    return res

null = None

root = [1,null,3,2,4,null,5,6]
Output = 3

root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output = 5

# root = []
# Output = []

start = build_tree(root)
print(print_tree(start))

sol = Solution()
res = sol.maxDepth(start)
print(res)
print(res == Output)
