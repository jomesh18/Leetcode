'''
  Binary Tree Postorder Traversal

Given the root of a binary tree, return the postorder traversal of its nodes' values.

 

Example 1:

Input: root = [1,null,2,3]
Output: [3,2,1]

Example 2:

Input: root = []
Output: []

Example 3:

Input: root = [1]
Output: [1]

Example 4:

Input: root = [1,2]
Output: [2,1]

Example 5:

Input: root = [1,null,2]
Output: [2,1]

 

Constraints:

	The number of the nodes in the tree is in the range [0, 100].
	-100 <= Node.val <= 100

 

Follow up:

Recursive solution is trivial, could you do it iteratively?

 

'''
# Definition for a binary tree node.
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

# class Solution:
#     def postorderTraversal(self, root: TreeNode) -> []:
#         return self.postorderTraversal(root.left)+self.postorderTraversal(root.right)+[root.val] if root else []

# iteratively using stack and visited flag
# class Solution:
# 	def postorderTraversal(self, root: TreeNode) -> []:
# 		stack, res = [(root, False)], []
# 		while stack:
# 			curr, visited = stack.pop()
# 			if curr:
# 				if visited:
# 					res.append(curr.val)
# 				else:
# 					stack.append((curr, True))
# 					stack.append((curr.right, False))
# 					stack.append((curr.left, False))
# 		return res

# iteratively using stack, not correct
class Solution:
	def postorderTraversal(self, root: TreeNode) -> []:
		nodes = []
		todo = []
		last = None
		while root or todo:
			if root:
				todo.append(root)
				root = root.left
			else:
				node = todo.pop()
				if node.right and last != node.right:
					root = node.right
				else:
					nodes.append(node.val)
					last = node
					todo.pop()
		return nodes

#from leetcode, modified pre order
# modified preorder (right subtree first). Then reverse the result.

# class Solution:
#     # @param {TreeNode} root
#     # @return {integer[]}
#     def postorderTraversal(self, root):
#         traversal, stack = [], [root]
#         while stack:
#             node = stack.pop()
#             if node:
#                 # pre-order, right first
#                 traversal.append(node.val)
#                 stack.append(node.left)
#                 stack.append(node.right)

#         # reverse result
#         return traversal[::-1]

tn = TreeNode('f', TreeNode('b', TreeNode('a', None, None), TreeNode('d', TreeNode('c', None, None), TreeNode('e', None, None))), TreeNode('g', None, TreeNode('i', TreeNode('h', None, None), None)))
s = Solution()
print(s.postorderTraversal(tn))
