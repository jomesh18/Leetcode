'''
897. Increasing Order Search Tree
Easy

3113

630

Add to List

Share
Given the root of a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only one right child.

 

Example 1:


Input: root = [5,3,6,2,4,null,8,1,null,null,null,7,9]
Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]
Example 2:


Input: root = [5,1,7]
Output: [1,null,5,null,7]
 

Constraints:

The number of nodes in the given tree will be in the range [1, 100].
0 <= Node.val <= 1000
Accepted
207,134
Submissions
264,806
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        
        def dfs(node):
            return dfs(node.left)+[node]+dfs(node.right) if node else []
        
        res = dfs(root)
        print([n.val for n in res])
        for i in range(len(res)-1):
            res[i].left = None
            res[i].right = res[i+1]
        res[-1].left = None
        return res[0]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def dfs(node):
            if not node: return None
            dfs(node.left)
            node.left = None
            self.curr.right = node
            self.curr = node
            dfs(node.right)

        dummy = TreeNode(0)
        self.curr = dummy
        dfs(root)
        return dummy.right

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        dummy = TreeNode(0)
        p = dummy
        curr = root
        stack = []
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            curr.left = None
            p.right = curr
            p = curr
            curr = curr.right
        return dummy.right
