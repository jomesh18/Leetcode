'''
Matchsticks to Square
You are given an integer array matchsticks where matchsticks[i] is the length of the ith matchstick. You want to use all the matchsticks to make one square. You should not break any stick, but you can link them up, and each matchstick must be used exactly one time.

Return true if you can make this square and false otherwise.

 

Example 1:


Input: matchsticks = [1,1,2,2,2]
Output: true
Explanation: You can form a square with length 2, one side of the square came two sticks with length 1.
Example 2:

Input: matchsticks = [3,3,3,3,4]
Output: false
Explanation: You cannot find a way to form a square with all the matchsticks.
 

Constraints:

1 <= matchsticks.length <= 15
0 <= matchsticks[i] <= 109
'''
#tle
# class Solution:
#     def makesquare(self, matchsticks: [int]) -> bool:
#         side = sum(matchsticks)/4
#         print(side)
#         if int(side) < side:
#             return False
#         # matchsticks.sort()
#         # if matchsticks[-1] > side:
#         #     return False
#         def helper(i, side1, side2, side3, side4):
#             print("helper({}, {}, {}, {}, {}".format(i, side1, side2, side3, side4))
#             if side1 == side or side2 == side or side3 == side or side4 == side:
#                 return True
#             if side1 > side or side2 > side or side3 > side or side4 > side:
#                 return False
#             if i > len(matchsticks):
#                 return False

#             return helper(i+1, side1+matchsticks[i], side2, side3, side4) or helper(i+1, side1, side2+matchsticks[i], side3, side4) or helper(i+1, side1, side2, side3+matchsticks[i], side4) or helper(i+1, side1, side2, side3, side4+matchsticks[i])
#         return helper(0, 0, 0, 0, 0)

# from leetcode, solution
class Solution:
    def makesquare(self, matchsticks: [int]) -> bool:
        """
        :type matchsticks: List[int]
        :rtype: bool
        """

        # If there are no matchsticks, then we can't form any square
        if not matchsticks:
            return False

        # Number of matchsticks we have
        L = len(matchsticks)

        # Perimeter of our square (if one can be formed)
        perimeter = sum(matchsticks)

        # number_of_units_per_boxPossible side of our square.
        possible_side =  perimeter // 4

        # If the perimeter can be equally split into 4 parts (and hence 4 sides, then we move on).
        if possible_side * 4 != perimeter:
            return False

        # Reverse sort the matchsticks because we want to consider the biggest one first.
        matchsticks.sort(reverse=True)

        # This array represents the 4 sides and their current lengths
        sums = [0 for _ in range(4)]

        # Our recursive dfs function.
        def dfs(index):

            # If we reach the end of matchsticks array, we check if the square was formed or not
            if index == L:
                # If 3 equal sides were formed, 4th will be the same as these three and answer should be True in that case.
                return sums[0] == sums[1] == sums[2] == possible_side

            # The current matchstick can belong to any of the 4 sides (provided their remaining lenghts are >= the size of the current matchstick)
            for i in range(4):
                # If this matchstick can fir in the space left for the current side
                if sums[i] + matchsticks[index] <= possible_side:
                    # Recurse
                    sums[i] += matchsticks[index]
                    if dfs(index + 1):
                        return True
                    # Revert the effects of recursion because we no longer need them for other recursions.
                    sums[i] -= matchsticks[index]
            return False        
        return dfs(0)

matchsticks = [1,1,2,2,2]
# Output: true

# matchsticks = [3,3,3,3,4]
# Output: false

matchsticks = [5969561,8742425,2513572,3352059,9084275,2194427,1017540,2324577,6810719,8936380,7868365,2755770,9954463,9912280,4713511]
print(len(matchsticks))

s = Solution()
print(s.makesquare(matchsticks))
