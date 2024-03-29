'''
Lowest Common Ancestor of a Binary Tree

Solution
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

 

Example 1:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
Example 2:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
Example 3:

Input: root = [1,2], p = 1, q = 2
Output: 1
 

Constraints:

The number of nodes in the tree is in the range [2, 105].
-109 <= Node.val <= 109
All Node.val are unique.
p != q
p and q will exist in the tree.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.path1, self.path2 = [], []
        self.found = 0
        def dfs(node, path):
            if not node: return
            if node == p or node == q:
                if self.found == 0:
                    self.path1 = path[:] + [node]
                    self.found = 1
                else:
                    self.path2 = path[:] + [node]
                    return
            dfs(node.left, path+[node])
            dfs(node.right, path+[node])

        dfs(root, [])
        ans = None
        for u, v in zip(self.path1, self.path2):
            if u.val != v.val:
                return ans
            ans = u
        return ans


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node):
            if not node: return None
            # If looking for me, return myself
            if node == p or node == q: return node
            # else look in left and right child
            l = dfs(node.left)
            r = dfs(node.right)
        # if both children returned a node, means
        # both p and q found so parent is LCA
            if l and r:
                return node

        # either one of the chidren returned a node, meaning either p or q found on left or right branch.
        # Example: assuming 'p' found in left child, right child returned 'None'. This means 'q' is
        # somewhere below node where 'p' was found we dont need to search all the way, 
        # because in such scenarios, node where 'p' found is LCA
            return l or r
        return dfs(root)