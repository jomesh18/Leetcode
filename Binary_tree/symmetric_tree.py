'''
  Symmetric Tree

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
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# iterative
# class Solution:
#     def isSymmetric(self, root: TreeNode) -> bool:
#         lef = deque([root.left])
#         rig = deque([root.right])
        
#         while lef or rig:
#             l = lef.popleft() if lef else None
#             r = rig.popleft() if rig else None
#             if l and r:
#                 if l.val != r.val:
#                     return False
#                 lef.extend([l.left, l.right])
#                 rig.extend([r.right, r.left])
#             elif not l and not r:
#                 pass
#             elif not l or not r:
#                 return False
#         return True

#from leetcode, using recursion
# class Solution:
#     def isSymmetric(self, root: TreeNode) -> bool:
#         return self.isMirror(root, root)

#     def isMirror(self, n1, n2):
#         if not n1 and not n2: return True
#         if not n1 or not n2: return False
#         return n1.val == n2.val and self.isMirror(n1.left, n2.right) and self.isMirror(n1.right, n2.left)

#from leetcode, using one queue
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        q = deque([root, root])
        while q:
            l = q.popleft()
            r = q.popleft()
            if not l and not r: continue
            if not l or not r: return False
            if l.val != r.val: return False
            q.extend([l.left, r.right, l.right, r.left])
        return True

#from leetcode
class Solution:
    def isSymmetric(self, root):
        def isSym(L,R):
            if L and R and L.val == R.val: 
                return isSym(L.left, R.right) and isSym(L.right, R.left)
            return L == R
        return not root or isSym(root.left, root.right)

#from leetcode, iterative
class Solution:
    def isSymmetric(self, root):
        queue = [root]
        while queue:
            values = [i.val if i else None for i in queue]
            if values != values[::-1]: return False
            queue = [child for i in queue if i for child in (i.left, i.right)]
        return True

def construct_tree(root):
    start = TreeNode(root[0])
    q = deque([start])
    i = 1
    while i < len(root):
        curr = q.popleft()
        if root[i] is not None:
            curr.left = TreeNode(root[i])
            q.append(curr.left)
        i += 1
        if root[i] is not None:
            curr.right = TreeNode(root[i])
            q.append(curr.right)
        i += 1
    return start

def print_level_order(root):
    level = [root]
    ans = []
    while root and level:
        ans.append([n.val for n in level])
        level = [n_l for n in level for n_l in (n.left, n.right) if n_l]
    return ans

root = [1,2,2,3,4,4,3]
# root = [1,2,2,3,None,3,None]
# Output: true
start = construct_tree(root)
print(print_level_order(start))
s = Solution()
print(s.isSymmetric(start))
