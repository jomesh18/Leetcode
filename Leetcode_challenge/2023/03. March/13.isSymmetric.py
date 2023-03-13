'''
101. Symmetric Tree
Easy

12659

285

Add to List

Share
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
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def helper(n1, n2):
            # print(n1.val if n1 else None, n2.val if n2 else None)
            if ((n1 and n2) and n1.val != n2.val) or (not n1 and n2) or (n1 and not n2):
                return False
            return not n1 or helper(n1.left, n2.right) and helper(n1.right, n2.left)
        return helper(root.left, root.right)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        q = deque([(root.left, root.right)])
        while q:
            l, r = q.popleft()
            if (l and r and l.val != r.val) or (not l and r) or (l and not r):
                return False
            if l:
                q.extend([(l.left, r.right), (l.right, r.left)])
        return True