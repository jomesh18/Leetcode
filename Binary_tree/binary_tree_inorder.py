'''
Binary Tree Inorder Traversal

Given the root of a binary tree, return the inorder traversal of its nodes' values.

 

Example 1:

Input: root = [1,null,2,3]
Output: [1,3,2]

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
Output: [1,2]

 

Constraints:

    The number of nodes in the tree is in the range [0, 100].
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

class Solution:
    def inorderTraversal(self, root: TreeNode) -> []:
        if not root:
            return root
        stack = [root]
        res = []
        traversed = []
        while stack:
            curr = stack.pop()
            if curr not in traversed:
                if curr.right:
                    stack.append(curr.right)
                stack.append(curr)
                if curr.left:
                    stack.append(curr.left)
                traversed.append(curr)
            else:
                res.append(curr.val)
            # print(stack, traversed, res)
        return res

tn = TreeNode('f', TreeNode('b', TreeNode('a', None, None), TreeNode('d', TreeNode('c', None, None), TreeNode('e', None, None))), TreeNode('g', None, TreeNode('i', TreeNode('h', None, None), None)))
s = Solution()
print(s.inorderTraversal(tn))

class Solution:
    def inorderTraversal(self, root: TreeNode) -> []:
    	res = []
    	self.dfs(root, res)
    	return res

    def dfs(self, root, res):
    	if not root:

    	res = dfs(root.left, res)+ root.val + dfs(root.right, res)

