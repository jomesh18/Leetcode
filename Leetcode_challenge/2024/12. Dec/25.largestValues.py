'''
515. Find Largest Value in Each Tree Row
Medium

3986

127

Add to List

Share
Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).

 

Example 1:


Input: root = [1,3,2,5,3,null,9]
Output: [1,3,9]
Example 2:

Input: root = [1,2,3]
Output: [1,3]
 

Constraints:

The number of nodes in the tree will be in the range [0, 104].
-231 <= Node.val <= 231 - 1
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        ans = []
        q = deque([root])
        while q:
            size = len(q)
            max_ = float('-inf')
            for _ in range(size):
                curr = q.popleft()
                max_ = max(curr.val, max_)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            ans.append(max_)
        return ans
    