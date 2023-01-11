'''
https://www.lintcode.com/problem/601/
601 · Flatten 2D Vector
Algorithms
Medium
Accepted Rate
54%
Description
Solution30
Notes99+
Discuss3
Leaderboard
Record
Description
Design an iterator to realize the function of flattening two-dimensional vector.

Example
Example 1:

Input:[[1,2],[3],[4,5,6]]
Output:[1,2,3,4,5,6]
Example 2:

Input:[[7,9],[5]]
Output:[7,9,5]
'''
class Vector2D(object):

    # @param vec2d {List[List[int]]}
    def __init__(self, vec2d):
        # Initialize your data structure here
        self.vec = vec2d
        self.pos = 0
        self.inside_pos = 0

    # @return {int} a next element
    def next(self):
        # Write your code here
        if self.hasNext():
            ans = self.vec[self.pos][self.inside_pos]
            self.inside_pos += 1
            return ans

    # @return {boolean} true if it has next element
    # or false
    def hasNext(self):
        # Write your code here
        while self.pos < len(self.vec):
            if len(self.vec[self.pos]) == self.inside_pos:
                self.inside_pos = 0
                self.pos += 1
            else:
                break
        return self.pos != len(self.vec)

# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())