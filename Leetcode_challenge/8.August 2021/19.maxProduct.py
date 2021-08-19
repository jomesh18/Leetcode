'''
Maximum Product of Splitted Binary Tree

Given the root of a binary tree, split the binary tree into two subtrees by removing one edge such that the product of the sums of the subtrees is maximized.

Return the maximum product of the sums of the two subtrees. Since the answer may be too large, return it modulo 109 + 7.

Note that you need to maximize the answer before taking the mod and not after taking it.

 

Example 1:

Input: root = [1,2,3,4,5,6]
Output: 110
Explanation: Remove the red edge and get 2 binary trees with sum 11 and 10. Their product is 110 (11*10)

Example 2:

Input: root = [1,null,2,3,4,null,null,5,6]
Output: 90
Explanation: Remove the red edge and get 2 binary trees with sum 15 and 6.Their product is 90 (15*6)

Example 3:

Input: root = [2,3,9,10,7,8,6,5,4,11,1]
Output: 1025

Example 4:

Input: root = [1,1]
Output: 1

 

Constraints:

    The number of nodes in the tree is in the range [2, 5 * 104].
    1 <= Node.val <= 104

'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxProduct(self, root) -> int:
        print(type(root))
        total = self.find_sum(root, 0)
        print(total)
        max_product = float("-inf")

    def find_sum(self, node, s):
        print(type(node))
        if not node:
            return 0
        s += node.val+self.find_sum(node.left, s)+self.find_sum(node.right, s)
        return s

def build_tree(root):
    start = TreeNode(root[0])
    q = [start]
    i = 1
    while i<len(root):
        curr = q.pop(0)
        if curr is not None:
            curr.left = TreeNode(root[i]) if root[i] is not None else None
            i += 1
            if i < len(root):
                curr.right = TreeNode(root[i]) if root[i] is not None else None
            q.extend([curr.left, curr.right])
        i += 1
    return start

def print_tree(start):
    res = []
    q = [start]
    while any(q):
        curr = q.pop(0)
        if curr:
            res.append(curr.val)
            q.extend([curr.left, curr.right])
        else:
            res.append(None)
    return res

root = [1,2,3,4,5,6]
# Output: 110

start = build_tree(root)
print(print_tree(start))

sol = Solution()
print(sol.maxProduct(start))
