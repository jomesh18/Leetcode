'''
Lowest Common Ancestor of a Binary Tree

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

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        curr = root
        def find(node):
        	res = set()
        	stack = [root]
        	while stack:
        		curr = stack.pop()
        		if curr == node:
        			break
        		
        	return res
        return (find(p) & find(s))

def build_tree(root):
	start = TreeNode(root[0])
	q = [start]
	i = 1
	while i<len(root):
		curr = q.pop(0)
		if curr:
			if root[i]: curr.left = TreeNode(root[i])
			i += 1
			if root[i]: curr.right = TreeNode(root[i])
			q.extend([curr.left, curr.right])
		i += 1
	return start

root = [3,5,1,6,2,0,8,None,None,7,4]
p = 5
q = 1
# Output: 3
start = build_tree(root)
s = Solution()
print(s.lowestCommonAncestor(start, TreeNode(p), TreeNode(q)).val)
