'''
Erect the Fence

You are given an array trees where trees[i] = [xi, yi] represents the location of a tree in the garden.

You are asked to fence the entire garden using the minimum length of rope as it is expensive. The garden is well fenced only if all the trees are enclosed.

Return the coordinates of trees that are exactly located on the fence perimeter.

 

Example 1:

Input: points = [[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]
Output: [[1,1],[2,0],[3,3],[2,4],[4,2]]

Example 2:

Input: points = [[1,2],[2,2],[4,2]]
Output: [[4,2],[2,2],[1,2]]

 

Constraints:

    1 <= points.length <= 3000
    points[i].length == 2
    0 <= xi, yi <= 100
    All the given points are unique.

'''
from functools import cmp_to_key
class Solution:
    def outerTrees(self, trees: [[int]]) -> [[int]]:
        def quater(p):
            x, y = p
            if x >= 0 and y >= 0: return 2
            if x < 0 and y >= 0: return 1
            if x < 0 and y < 0: return 4
            if x >= 0 and y < 0: return 3

        def compare(p1, p2):
            if quater(p1) == quater(p2):
                t1 = p1[1]*p2[0] - p2[1]*p1[0]
                return  1 - 2*int((-p1[1], p1[0]) < (-p2[1], p2[0])) if t1 == 0 else 1 if t1 > 0 else -1
            else:
                return 1 if quater(p1) < quater(p2) else -1
        
        def cross(p1, p2, p3):
            return (p2[0]-p1[0])*(p3[1]-p1[1])-(p2[1]-p1[1])*(p3[0]-p1[0])

        start = min(trees)
        trees.pop(trees.index(start))
        trees = [[x - start[0], y - start[1]] for x, y in trees]
        trees.sort(key = cmp_to_key(compare))

        ans = [[0, 0]]
        for p in trees:
            ans.append(p)
            while len(ans) > 2 and cross(*ans[-3:]) < 0:
                ans.pop(-2)
        
        return [[x + start[0], y + start[1]] for x, y in ans]

trees = [[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]
# Output: [[1,1],[2,0],[3,3],[2,4],[4,2]]

trees = [[1,2],[2,2],[4,2]]
# Output: [[4,2],[2,2],[1,2]]

sol = Solution()
print(sol.outerTrees(trees))
