'''
849. Maximize Distance to Closest Person
Medium

1728

145

Add to List

Share
You are given an array representing a row of seats where seats[i] = 1 represents a person sitting in the ith seat, and seats[i] = 0 represents that the ith seat is empty (0-indexed).

There is at least one empty seat, and at least one person sitting.

Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized. 

Return that maximum distance to the closest person.

 

Example 1:


Input: seats = [1,0,0,0,1,0,1]
Output: 2
Explanation: 
If Alex sits in the second open seat (i.e. seats[2]), then the closest person has distance 2.
If Alex sits in any other open seat, the closest person has distance 1.
Thus, the maximum distance to the closest person is 2.
Example 2:

Input: seats = [1,0,0,0]
Output: 3
Explanation: 
If Alex sits in the last seat (i.e. seats[3]), the closest person is 3 seats away.
This is the maximum distance possible, so the answer is 3.
Example 3:

Input: seats = [0,1]
Output: 1
 

Constraints:

2 <= seats.length <= 2 * 104
seats[i] is 0 or 1.
At least one seat is empty.
At least one seat is occupied.
'''
#two pass, O(n) time, O(1) space
# class Solution:
#     def maxDistToClosest(self, seats: List[int]) -> int:
#         last_person_position_to_left = float("-inf")
#         for i in range(len(seats)):
#             if seats[i]:
#                 last_person_position_to_left = i
#             else:
#                 seats[i] = last_person_position_to_left-i
#         last_person_position_to_right = float("inf")
#         max_dist = float("inf")
#         for i in range(len(seats)-1, -1, -1):
#             if seats[i] == 1:
#                 last_person_position_to_right = i
#             else:
#                 seats[i] = max((i - last_person_position_to_right), seats[i])
#                 max_dist = min(seats[i], max_dist)
#         return -max_dist

#from leetcode solution
# class Solution(object):
#     def maxDistToClosest(self, seats):
#         people = (i for i, seat in enumerate(seats) if seat)
#         prev, future = None, next(people)

#         ans = 0
#         for i, seat in enumerate(seats):
#             if seat:
#                 prev = i
#             else:
#                 while future is not None and future < i:
#                     future = next(people, None)

#                 left = float('inf') if prev is None else i - prev
#                 right = float('inf') if future is None else future - i
#                 ans = max(ans, min(left, right))

#         return ans


#One pass, O(n)
class Solution(object):
    def maxDistToClosest(self, seats):
        last = -1
        ans = 0
        for i in range(len(seats)):
            if seats[i]:
                ans = max(ans, i if last < 0 else (i-last)//2)
                last = i
        return max(ans, len(seats)-1-last)

seats = [1,0,0,0,1,0,1]
# Output: 2

# seats = [1,0,0,0]
# # Output: 3

# seats = [0,1]
# # Output: 1

sol = Solution()
print(sol.maxDistToClosest(seats))
