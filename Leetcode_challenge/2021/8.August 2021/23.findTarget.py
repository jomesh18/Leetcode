'''
Two Sum IV - Input is a BST

Given the root of a Binary Search Tree and a target number k, return true if there exist two elements in the BST such that their sum is equal to the given target.

 

Example 1:

Input: root = [5,3,6,2,4,null,7], k = 9
Output: true

Example 2:

Input: root = [5,3,6,2,4,null,7], k = 28
Output: false

Example 3:

Input: root = [2,1,3], k = 4
Output: true

Example 4:

Input: root = [2,1,3], k = 1
Output: false

Example 5:

Input: root = [2,1,3], k = 3
Output: true

 

Constraints:

    The number of nodes in the tree is in the range [1, 104].
    -104 <= Node.val <= 104
    root is guaranteed to be a valid binary search tree.
    -105 <= k <= 105

'''

# Definition for a binary tree node.
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findTarget(self, root, k) -> bool:
        def find(root, val, old):
            if not root: return False
            if val > root.val:
                return find(root.right, val, old)
            elif val < root.val:
                return find(root.left, val, old)
            else:
                if old != root:
                    return True
                else:
                    return (find(root.left, val, old) or find(root.right, val, old))
        q = deque([root])
        while q:
            curr = q.popleft()
            if curr:
                if find(root, k-curr.val, curr):
                    return True
                q.extend([curr.left, curr.right])
        return False


#from leetcode, fastest
from collections import deque
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        s = set()
        q = deque()
        q.append(root)
        #when q has elements on it, it will return True; otherwise, it's false.
        while q:
            temp = q.popleft()
            if temp.val in s:
                return True
            else:
                s.add(k-temp.val)
                if temp.left is not None:
                    q.append(temp.left)
                if temp.right is not None:
                    q.append(temp.right)          
        return False
def build_tree(root):
    start = TreeNode(root[0])
    q = deque([start])
    i = 1
    while i<len(root):
        curr = q.popleft()
        if curr:
            curr.left = TreeNode(root[i]) if root[i] is not None else None
            i += 1
            q.append(curr.left)
            if i < len(root):
                curr.right = TreeNode(root[i]) if root[i] is not None else None
                i += 1
                q.append(curr.right)
    return start

def print_tree(start):
    res = []
    q = deque([start])
    while any(q):
        curr = q.popleft()
        if curr:
            res.append(curr.val)
            q.extend([curr.left, curr.right])
        else:
            res.append(None)
    return res

null = None

root = [5,3,6,2,4,null,7]
k = 9
# Output: true

root = [5,3,6,2,4,null,7]
k = 28
# # Output: false

root = [2,1,3]
k = 4
# # Output: true

root = [2,1,3]
k = 1
# # Output: false

root = [2,1,3]
k = 3
# # Output: true

root = [1]
k = 2
#Output: false

start = build_tree(root)
print(print_tree(start))

sol = Solution()
print(sol.findTarget(start, k))
