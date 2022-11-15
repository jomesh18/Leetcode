'''
222. Count Complete Tree Nodes
Medium

6150

350

Add to List

Share
Given the root of a complete binary tree, return the number of the nodes in the tree.

According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Design an algorithm that runs in less than O(n) time complexity.

 

Example 1:


Input: root = [1,2,3,4,5,6]
Output: 6
Example 2:

Input: root = []
Output: 0
Example 3:

Input: root = [1]
Output: 1
 

Constraints:

The number of nodes in the tree is in the range [0, 5 * 104].
0 <= Node.val <= 5 * 104
The tree is guaranteed to be complete.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# bfs
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        q = [root]
        level = 0
        broken = False
        while not broken:
            newq = []
            for node in q:
                if node.left:
                    newq.append(node.left)
                else:
                    broken = True
                    break
                if node.right:
                    newq.append(node.right)
                else:
                    broken = True
                    break
            level += 1
            q = newq[:]
        # print(level, q)
        return (2**level)-1 + len(q)

# dfs
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node: return 0
            if not node.left: return 1
            if not node.right: return 2
            return 1 + dfs(node.left) + dfs(node.right)
        return dfs(root)


# binary search O(log n)* (log n)
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        def path(num, root):
            for i in bin(num)[3:]:
                if i == '0':
                    root = root.left
                else:
                    root = root.right
                if not root: return False
            return True
        depth = 0
        curr = root
        while curr and curr.left:
            depth += 1
            curr = curr.left
        begin, end = 1<<depth, 1<<(depth+1)
        ans = begin
        while begin < end:
            mid = (begin+end)//2
            if not path(mid, root):
                end = mid
            else:
                begin = mid + 1
        return begin - 1


# O(log n)* (log n)
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        left_depth = self.find_depth(root.left)
        right_depth = self.find_depth(root.right)
        if left_depth == right_depth:
            return (1 << left_depth) + self.countNodes(root.right)
        else:
            return (1 << right_depth) + self.countNodes(root.left)

    def find_depth(self, root):
        if not root: return 0
        return 1 + self.find_depth(root.left)
