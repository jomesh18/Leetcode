'''
607 · Two Sum III - Data structure designPRE
Algorithms
Easy
Accepted Rate43%
Description
Solution
Notes
Discuss
Leaderboard
This topic is a pre-release topic. If you encounter any problems, please contact us via "Problem Correction", and we will upgrade your account to VIP as a thank you.
Description

Design and implement a TwoSum class. It should support the following operations: add and find.

add - Add the number to an internal data structure.
find - Find if there exists any pair of numbers which sum is equal to the value.
Example

Example 1:

add(1); add(3); add(5);

find(4) // return true

find(7) // return false
'''
from collections import defaultdict
class TwoSum:
    """
    @param number: An integer
    @return: nothing
    """

    def __init__(self):
        self.d = defaultdict(int)

    def add(self, number):
        # write your code here
        self.d[number] += 1

    """
    @param value: An integer
    @return: Find if there exists any pair of numbers which sum is equal to the value.
    """
    def find(self, value):
        # write your code here
        for num in self.d:
            if (value-num != num and value-num in self.d) or (value-num == num and self.d[num] > 1):
                return True
        return False
