'''
Binary Tree Preorder Traversal

Given the root of a binary tree, return the preorder traversal of its nodes' values.

 

Example 1:

Input: root = [1,null,2,3]
Output: [1,2,3]

Example 2:

Input: root = []
Output: []

Example 3:

Input: root = [1]
Output: [1]

Example 4:

Input: root = [1,2]
Output: [1,2]

Example 5:

Input: root = [1,null,2]
Output: [1,2]

 

Constraints:

	The number of nodes in the tree is in the range [0, 100].
	-100 <= Node.val <= 100

 

Follow up: Recursive solution is trivial, could you do it iteratively?
'''
# Definition for a binary tree node.
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right
# iterative
# class Solution:
#     def preorderTraversal(self, root: TreeNode) -> []:
#         if not root:
#             return []
#         stack = [root]
#         res = []
#         while stack:
#             curr = stack.pop()
#             res.append(curr.val)
#             if curr.right:
#                 stack.append(curr.right)
#             if curr.left:
#                 stack.append(curr.left)
#         return res
# recursive
class Solution:
	res = []
	def preorderTraversal(self, root: TreeNode) -> []:
		if not root:
			return []
		self.res.append(root.val)
		if root.left:
			self.preorderTraversal(root.left)
		if root.right:
			self.preorderTraversal(root.right)
		return self.res

# root = [1, None, 2]
root = TreeNode(1, None, TreeNode(2, None, None))
s = Solution()
print(s.preorderTraversal(root))


# from leetcode
# recursively
def preorderTraversal1(self, root):
    res = []
    self.dfs(root, res)
    return res
    
def dfs(self, root, res):
    if root:
        res.append(root.val)
        self.dfs(root.left, res)
        self.dfs(root.right, res)

# iteratively
def preorderTraversal(self, root):
    stack, res = [root], []
    while stack:
        node = stack.pop()
        if node:
            res.append(node.val)
            stack.append(node.right)
            stack.append(node.left)
    return res
