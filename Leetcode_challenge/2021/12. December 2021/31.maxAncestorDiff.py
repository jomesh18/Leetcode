'''

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.min = float("-inf")
        def traversal(node, min_, max_):
            if not node: return
            self.min = max(self.min, abs(node.val-min_), abs(node.val-max_))
            # print(self.min)
            traversal(node.left, min(min_, node.val), max(max_, node.val))
            traversal(node.right, min(min_, node.val), max(max_, node.val))
        traversal(root.left, root.val, root.val)
        traversal(root.right, root.val, root.val)
        return self.min


#from leetcode, solution 1
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        if not root:
            return 0
        # record the required maximum difference
        self.result = 0

        def helper(node, cur_max, cur_min):
            if not node:
                return
            # update `result`
            self.result = max(self.result, abs(cur_max-node.val),
                              abs(cur_min-node.val))
            # update the max and min
            cur_max = max(cur_max, node.val)
            cur_min = min(cur_min, node.val)
            helper(node.left, cur_max, cur_min)
            helper(node.right, cur_max, cur_min)

        helper(root, root.val, root.val)
        return self.result

#from leetcode, solution 2
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        if not root: return 0
        def helper(node, curr_min, curr_max):
            if not node:
                return curr_max-curr_min
            curr_max = max(curr_max, node.val)
            curr_min = min(curr_min, node.val)
            return max(helper(node.left, curr_min, curr_max), helper(node.right, curr_min, curr_max))
        return helper(root, root.val, root.val)
