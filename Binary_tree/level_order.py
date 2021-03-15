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
        while not all(l is None for l in queue):
            temp_queue = []
            temp_res = []
            while queue:
                curr = queue.pop(0)
                temp_res.append(curr.val)
                if curr.left:
                    temp_queue.append(curr.left)
                if curr.right:
                    temp_queue.append(curr.right)
            res.append(temp_res)
            queue.extend(temp_queue)
        return res

#from leetcode
# level is a list of the nodes in the current level. Keep appending a list of the values of these nodes to ans and then updating level with all the nodes in the next level (kids) until it reaches an empty level. Python's list comprehension makes it easier to deal with many conditions in a concise manner.


# Solution 1, (6 lines)

def levelOrder(self, root):
    ans, level = [], [root]
    while root and level:
        ans.append([node.val for node in level])
        LRpair = [(node.left, node.right) for node in level]
        level = [leaf for LR in LRpair for leaf in LR if leaf]
    return ans


# Solution 2, (5 lines), same idea but use only one list comprehension in while loop to get the next level

def levelOrder(self, root):
    ans, level = [], [root]
    while root and level:
        ans.append([node.val for node in level])            
        level = [kid for n in level for kid in (n.left, n.right) if kid]
    return ans


# Solution 3 (10 lines), just an expansion of solution 1&2 for better understanding.

def levelOrder(self, root):
    if not root:
        return []
    ans, level = [], [root]
    while level:
        ans.append([node.val for node in level])
        temp = []
        for node in level:
            temp.extend([node.left, node.right])
        level = [leaf for leaf in temp if leaf]
    return ans

# root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]

# tree = TreeNode(3, TreeNode(9, None, None), TreeNode(20, TreeNode(15, None, None), TreeNode(7, None, None)))
tree = None
s = Solution()
res = s.levelOrder(tree)
print(res)
