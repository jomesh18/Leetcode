'''
100. Same Tree
Easy

11083

228

Add to List

Share
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

 

Example 1:


Input: p = [1,2,3], q = [1,2,3]
Output: true
Example 2:


Input: p = [1,2], q = [1,null,2]
Output: false
Example 3:


Input: p = [1,2,1], q = [1,1,2]
Output: false
 

Constraints:

The number of nodes in both trees is in the range [0, 100].
-104 <= Node.val <= 104
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        q1, q2 = deque([p]), deque([q])
        while q1 and q2:
            c1, c2 = q1.popleft(), q2.popleft()
            if (c1 and c2 and c1.val != c2.val) or (bool(c1) ^ bool(c2)):
                return False
            if c1:
                q1.append(c1.left)
                q1.append(c1.right)
                q2.append(c2.left)
                q2.append(c2.right)
        return q1 == q2