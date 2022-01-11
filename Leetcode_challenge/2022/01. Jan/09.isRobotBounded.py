'''
1041. Robot Bounded In Circle
Medium

2694

582

Add to List

Share
On an infinite plane, a robot initially stands at (0, 0) and faces north. The robot can receive one of three instructions:

"G": go straight 1 unit;
"L": turn 90 degrees to the left;
"R": turn 90 degrees to the right.
The robot performs the instructions given in order, and repeats them forever.

Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.

 

Example 1:

Input: instructions = "GGLLGG"
Output: true
Explanation: The robot moves from (0,0) to (0,2), turns 180 degrees, and then returns to (0,0).
When repeating these instructions, the robot remains in the circle of radius 2 centered at the origin.
Example 2:

Input: instructions = "GG"
Output: false
Explanation: The robot moves north indefinitely.
Example 3:

Input: instructions = "GL"
Output: true
Explanation: The robot moves from (0, 0) -> (0, 1) -> (-1, 1) -> (-1, 0) -> (0, 0) -> ...
 

Constraints:

1 <= instructions.length <= 100
instructions[i] is 'G', 'L' or, 'R'.
Accepted
168,808
Submissions
303,753
'''
# class Solution:
#     def isRobotBounded(self, instructions: str) -> bool:
#         x, y, d = 0, 0, [(0, 1), (1, 0), (0, -1), (-1, 0)]
#         i = 0
#         for inst in instructions:
#             if inst == "L":
#                 i = (i+3)%4
#             elif inst == "R":
#                 i = (i+1) % 4
#             else:
#                 x += d[i][0]
#                 y += d[i][1]
#         return (x, y) == (0, 0) or i > 0

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x, y = 0, 0
        dx, dy = 0, 1
        for inst in instructions:
            if inst == "L":
                dx, dy = -dy, dx
            elif inst = "R":
                dx, dy = dy, -dx
            else:
                x += dx
                y += dy
        return (x, y) = (0, 0) or (dx, dy) != (0, 1)

instructions = "GGLLGG"
# Output: true

# instructions = "GG"
# Output: false

# instructions = "GL"
# Output: true

sol = Solution()
print(sol.isRobotBounded(instructions))
