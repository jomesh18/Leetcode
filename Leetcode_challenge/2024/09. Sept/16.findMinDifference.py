'''
539. Minimum Time Difference
Medium

2048

281

Add to List

Share
Given a list of 24-hour clock time points in "HH:MM" format, return the minimum minutes difference between any two time-points in the list.
 

Example 1:

Input: timePoints = ["23:59","00:00"]
Output: 1
Example 2:

Input: timePoints = ["00:00","23:59","00:00"]
Output: 0
 

Constraints:

2 <= timePoints.length <= 2 * 104
timePoints[i] is in the format "HH:MM".
'''
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints.sort()
        least_diff = 1440
        def find_min_mins(t1, t2):
            hours = int(t2[:2])-int(t1[:2])
            mins = int(t2[3:])-int(t1[3:])
            curr_mins = hours * 60 + mins
            return min(curr_mins, 1440-curr_mins)
        
        for i in range(1, len(timePoints)):
            curr_diff = find_min_mins(timePoints[i-1], timePoints[i])
            least_diff = min(least_diff, curr_diff)
        
        least_diff = min(least_diff, find_min_mins(timePoints[0], timePoints[-1]))
        return least_diff
    