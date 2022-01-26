'''
1305. All Elements in Two Binary Search Trees
Medium

1724

53

Add to List

Share
Given two binary search trees root1 and root2, return a list containing all the integers from both trees sorted in ascending order.

 

Example 1:


Input: root1 = [2,1,4], root2 = [1,0,3]
Output: [0,1,1,2,3,4]
Example 2:


Input: root1 = [1,null,8], root2 = [8,1]
Output: [1,1,8,8]
 

Constraints:

The number of nodes in each tree is in the range [0, 5000].
-105 <= Node.val <= 105
Accepted
128,668
Submissions
162,262
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        
        def dfs(node):
            stack, res = [], []
            while stack or node:
                while node:
                    stack.append(node)
                    node = node.left
                node = stack.pop()
                res.append(node.val)
                node = node.right
            return res
        list1, list2 = dfs(root1), dfs(root2)
        
        res = []
        i, j = 0, 0
        while i < len(list1) and j < len(list2):
            if list1[i] <= list2[j]:
                res.append(list1[i])
                i += 1
            else:
                res.append(list2[j])
                j += 1
        if i == len(list1):
            res.extend(list2[j:])
        elif j == len(list2):
            res.extend(list1[i:])
        return res


class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        values = []
        def collect(root):
            if root:
                collect(root.left)
                values.append(root.val)
                collect(root.right)
        collect(root1)
        collect(root2)
        return sorted(values)