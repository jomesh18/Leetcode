'''
Same Tree

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
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#recursive
# class Solution:
#     def isSameTree(self, p, q) -> bool:
#         if not p and not q: return True
#         if not p or not q: return False
#         if p.val == q.val:
#             return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
#         return False

#iterative
class Solution:
    def isSameTree(self, p, q) -> bool:
        def check_pq(p, q):
            if not p and not q: return True
            if not p or not q: return False
            if p.val != q.val: return False
            return True

        deq = deque([(p, q)])
        while deq:
            p, q = deq.popleft()
            if not check_pq(p, q):
                return False
            if p:
                deq.append((p.left, q.left))
                deq.append((p.right, q.right))
        return True

def build_tree(l):
    if not l: return []
    start = TreeNode(l[0])
    i = 1
    q = deque([start])
    while i < len(l):
        curr = q.popleft()
        if curr:
            curr.left = TreeNode(l[i]) if l[i] is not None else None
            q.append(curr.left)
            i += 1
            if i < len(l):
                curr.right = TreeNode(l[i] if l[i] is not None else None)
                q.append(curr.right)
                i += 1
    return start

def print_tree(root):
    res = []
    q = deque([root])
    while any(q):
        curr = q.popleft()
        if curr:
            res.append(curr.val)
            q.extend([curr.left, curr.right])
        else:
            res.append(None)
    return res

null = None
false = False
true = True

p = [1,2,3]
q = [1,2,3]
# Output: true

# p = [1,2]
# q = [1,null,2]
# # Output: false

p = [1,2,1]
q = [1,1,2]
# Output: false

p_start = build_tree(p)
q_start = build_tree(q)

print(print_tree(p_start))
print(print_tree(q_start))

sol = Solution()
print(sol.isSameTree(p_start, q_start))
