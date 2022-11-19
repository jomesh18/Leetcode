'''
587. Erect the Fence
Hard

966

532

Add to List

Share
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
class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        trees = sorted(set((i, j) for i, j in trees), key=lambda p: (p[0], p[1]))
        def cross(o, a, b):
            return (a[0]-o[0])*(b[1]-o[1]) - (a[1]-o[1])*(b[0]-o[0])
        lower = []
        for t in trees:
            while len(lower) >= 2 and cross(lower[-2], lower[-1], t) < 0:
                lower.pop()
            lower.append(t)
            
        upper = []
        for t in reversed(trees):
            while len(upper) >= 2 and cross(upper[-2], upper[-1], t) < 0:
                upper.pop()
            upper.append(t)
        print(lower, upper)
        return [[i, j] for i, j in set(lower+upper)]