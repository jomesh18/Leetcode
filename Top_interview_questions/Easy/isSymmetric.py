'''
Symmetric Tree

Solution
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

 

Example 1:


Input: root = [1,2,2,3,4,4,3]
Output: true
Example 2:


Input: root = [1,2,2,null,3,null,3]
Output: false
 

Constraints:

The number of nodes in the tree is in the range [1, 1000].
-100 <= Node.val <= 100
 

Follow up: Could you solve it both recursively and iteratively?
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#recursive
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def helper(left, right):
            if not left and not right: return True
            if (not left and right) or (not right and left): return False
            if left.val != right.val: return False
            return helper(left.left, right.right) and helper(left.right, right.left)
        return helper(root.left, root.right)

#iterative
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        stack = [(root.left, root.right)]

        while stack:
            left, right = stack.pop()
            if not left and not right: continue
            if (not left and right) or (not right and left): return False
            if left.val != right.val: return False
            stack.extend([(left.right, right.left), (left.left, right.right)])
        return True

#consice recursive, fastest
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def test(left, right):
            if left == None and right == None:
                return True
            elif left != None and right != None:
                return (left.val == right.val and test(left.left,right.right) and test(left.right, right.left))
            
            return False
                
        if not root:
            return True
        return test(root.left, root.right)