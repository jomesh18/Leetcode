'''
100. Same Tree
Easy

8261

167

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
        def bfs(node):
            if not node: return []
            q = [node]
            res = []
            while q:
                newq = []
                t = []
                for nod in q:
                    t.append(nod.val if nod else None)
                    if nod:
                        newq.append(nod.left if nod.left else None)
                        newq.append(nod.right if nod.right else None)
                res.extend(t)
                q = newq[:]
            return res
                
        return bfs(p) == bfs(q)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: return True
        if not p or not q: return False
        if p.val != q.val: return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def check(p, q):
            if not p and not q: return True
            if not p or not q: return False
            if p.val != q.val: return False
            return True
        qu = deque([(p, q)])
        while qu:
            p, q = qu.popleft()
            if not check(p, q):
                return False
            if p:
                qu.append((p.left, q.left))
                qu.append((p.right, q.right))
        return True