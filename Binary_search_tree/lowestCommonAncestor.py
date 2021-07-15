'''
Lowest Common Ancestor of a Binary Search Tree

Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

 

Example 1:

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.

Example 2:

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.

Example 3:

Input: root = [2,1], p = 2, q = 1
Output: 2

 

Constraints:

    The number of nodes in the tree is in the range [2, 105].
    -109 <= Node.val <= 109
    All Node.val are unique.
    p != q
    p and q will exist in the BST.

'''

# Definition for a binary tree node.
from collections import deque
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# class Solution(object):
#     def lowestCommonAncestor(self, root, p, q):
#         """
#         :type root: TreeNode
#         :type p: TreeNode
#         :type q: TreeNode
#         :rtype: TreeNode
#         """
#         def find_node_path(root, node, path):
#             if not root:
#                 return None
#             path.append(root)
#             # print(path)
#             if root.val == node.val:
#                 return path
#             elif root.val < node.val:
#                 return find_node_path(root.right, node, path)
#             else:
#                 return find_node_path(root.left, node, path)
#         l1 = find_node_path(root, p, [])
#         l2 = find_node_path(root, q, [])
#         # print(l1, l2)
#         ans = l1[0]
#         for u, v in zip(l1, l2):
#             if u.val == v.val:
#                 ans = u
#             else:
#                 break
#         return ans

#recursive
# class Solution(object):
#     def lowestCommonAncestor(self, root, p, q):
#         """
#         :type root: TreeNode
#         :type p: TreeNode
#         :type q: TreeNode
#         :rtype: TreeNode
#         """
#         if p.val>root.val and q.val>root.val:
#             return self.lowestCommonAncestor(root.right, p, q)
#         elif p.val<root.val and q.val<root.val:
#             return self.lowestCommonAncestor(root.left, p, q)
#         else:
#             return root

#iterative
# class Solution(object):
#     def lowestCommonAncestor(self, root, p, q):
#         while root:
#             if p.val > root.val and q.val>root.val:
#                 root = root.right
#             elif p.val<root.val and q.val<root.val:
#                 root = root.left
#             else:
#                 return root

#stefan pochmann
# def lowestCommonAncestor(self, root, p, q):
#     while (root.val - p.val) * (root.val - q.val) > 0:
#         root = (root.left, root.right)[p.val > root.val]
#     return root

# def lowestCommonAncestor(self, root, p, q):
#     next = p.val < root.val > q.val and root.left or \
#            p.val > root.val < q.val and root.right
#     return self.lowestCommonAncestor(next, p, q) if next else root

# def lowestCommonAncestor(self, root, p, q):
#     return root if (root.val - p.val) * (root.val - q.val) < 1 else \
#            self.lowestCommonAncestor((root.left, root.right)[p.val > root.val], p, q)

def build_tree(root):
    start = TreeNode(root[0])
    q = deque([start])
    i = 1
    while i<len(root):
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

root = [6,2,8,0,4,7,9,null,null,3,5]
p = 2
q = 8
# Output: 6

# root = [6,2,8,0,4,7,9,null,null,3,5]
# p = 2
# q = 4
# # Output: 2

# root = [2,1]
# p = 2
# q = 1
# # Output: 2

start = build_tree(root)
print(print_tree(start))

s = Solution()
print(s.lowestCommonAncestor(start, TreeNode(p), TreeNode(q)).val)
