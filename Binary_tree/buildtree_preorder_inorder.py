'''
Construct Binary Tree from Preorder and Inorder Traversal

Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

 

Example 1:

Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]

Example 2:

Input: preorder = [-1], inorder = [-1]
Output: [-1]

 

Constraints:

    1 <= preorder.length <= 3000
    inorder.length == preorder.length
    -3000 <= preorder[i], inorder[i] <= 3000
    preorder and inorder consist of unique values.
    Each value of inorder also appears in preorder.
    preorder is guaranteed to be the preorder traversal of the tree.
    inorder is guaranteed to be the inorder traversal of the tree.

'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# class Solution:
#     def buildTree(self, preorder: [], inorder: []) -> TreeNode:
#     	if not inorder: return None
#     	ind = inorder.index(preorder.pop(0))
#     	root = TreeNode(inorder[ind])
#     	root.left = self.buildTree(preorder[:ind], inorder[:ind])
#     	root.right = self.buildTree(preorder[ind:], inorder[ind+1:])
#     	return root

# class Solution:
#     def buildTree(self, preorder: [], inorder: []) -> TreeNode:
#     	if inorder:
#     		ind = inorder.index(preorder.pop(0))
#     		root = TreeNode(inorder[ind])
#     		root.left = self.buildTree(preorder, inorder[:ind])
#     		root.right = self.buildTree(preorder, inorder[ind+1:])
#     		return root
    	
class Solution:
    def buildTree(self, preorder: [], inorder: []) -> TreeNode:
    	dict = {value: ind for ind, value in enumerate(inorder)}
    	def build(pre_beg, pre_end, in_beg, in_end):
    		if not in_end<=in_beg:
    			return None
    		root = TreeNode(dict[pre_beg])
    		root.left = build(pre_beg+1)
    		root.right = 

    	return build(0, len(preorder), 0, len(inorder))

def print_tree(ans):
	q = [ans]
	res = []
	while any(q):
		curr = q.pop(0)
		if curr:
			res.append(curr.val)
			q.extend([curr.left, curr.right])
		else: res.append(None)
	return res

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
# Output: [3,9,20,null,null,15,7]
s = Solution()
ans = s.buildTree(preorder, inorder)
print(print_tree(ans))
        