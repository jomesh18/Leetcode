'''
Binary Tree Level Order Traversal

Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

 

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Example 2:

Input: root = [1]
Output: [[1]]

Example 3:

Input: root = []
Output: []

 

Constraints:

    The number of nodes in the tree is in the range [0, 2000].
    -1000 <= Node.val <= 1000


'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: TreeNode) -> [[]]:
        queue = [root]
        res = []
        count = 1
        while queue and count<15:
            # print('Count {}'.format(count))
            count += 1
            curr = queue.pop(0)
            level_res = []
            level_q = []
            # print("Curr: {}".format(curr))
            for i in curr:
                if i:
                    # print('val of i is {}'.format(i.val))
                    level_res.append(i.val)
                    # print('level_res is {}'.format(level_res))
                    level_q.append(i.left)
                    level_q.append(i.right)
                    # print('level_q is {}'.format(level_q))
            res.append(level_res)
            queue.append(level_q)
            # level_q.clear()
            # level_res.clear()
            # print('res is {} and queue is {}'.format(res, queue))
        return res

# root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]

tree = TreeNode(3, TreeNode(9, None, None), TreeNode(20, TreeNode(15, None, None), TreeNode(7, None, None)))
s = Solution()
res = s.levelOrder(tree)
print(res)
