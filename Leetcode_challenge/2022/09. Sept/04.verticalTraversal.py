'''
987. Vertical Order Traversal of a Binary Tree
Hard

5168

3952

Add to List

Share
Given the root of a binary tree, calculate the vertical order traversal of the binary tree.

For each node at position (row, col), its left and right children will be at positions (row + 1, col - 1) and (row + 1, col + 1) respectively. The root of the tree is at (0, 0).

The vertical order traversal of a binary tree is a list of top-to-bottom orderings for each column index starting from the leftmost column and ending on the rightmost column. There may be multiple nodes in the same row and same column. In such a case, sort these nodes by their values.

Return the vertical order traversal of the binary tree.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]
Explanation:
Column -1: Only node 9 is in this column.
Column 0: Nodes 3 and 15 are in this column in that order from top to bottom.
Column 1: Only node 20 is in this column.
Column 2: Only node 7 is in this column.
Example 2:


Input: root = [1,2,3,4,5,6,7]
Output: [[4],[2],[1,5,6],[3],[7]]
Explanation:
Column -2: Only node 4 is in this column.
Column -1: Only node 2 is in this column.
Column 0: Nodes 1, 5, and 6 are in this column.
          1 is at the top, so it comes first.
          5 and 6 are at the same position (2, 0), so we order them by their value, 5 before 6.
Column 1: Only node 3 is in this column.
Column 2: Only node 7 is in this column.
Example 3:


Input: root = [1,2,3,4,6,5,7]
Output: [[4],[2],[1,5,6],[3],[7]]
Explanation:
This case is the exact same as example 2, but with nodes 5 and 6 swapped.
Note that the solution remains the same since 5 and 6 are in the same location and should be ordered by their values.
 

Constraints:

The number of nodes in the tree is in the range [1, 1000].
0 <= Node.val <= 1000
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = [(root, 0)]
        d = defaultdict(list)
        while q:
            newq = []
            t = defaultdict(list)
            for node, col in q:
                t[col].append(node.val)
                if node.left:
                    newq.append((node.left, col-1))
                if node.right:
                    newq.append((node.right, col+1))
            q = newq[:]
            for col in t:
                d[col].extend(sorted(t[col]))
        # print(d)
        return [d[key] for key in sorted(d.keys())]

#dfs
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        d = defaultdict(list)
        self.minc = float('inf')
        self.maxc = float('-inf')
        def dfs(node, r, c):
            self.minc = min(self.minc, c)
            self.maxc = max(self.maxc, c)
            d[c].append((r, node.val))
            if node.left: dfs(node.left, r+1, c-1)
            if node.right: dfs(node.right, r+1, c+1)
        
        dfs(root, 0, 0)
        res = []
        for c in range(self.minc, self.maxc+1):
            res.append([v for r, v in sorted(d[c])])
        return res
        