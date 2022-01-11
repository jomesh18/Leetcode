'''
Sum of Square Numbers

Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.

 

Example 1:

Input: c = 5
Output: true
Explanation: 1 * 1 + 2 * 2 = 5

Example 2:

Input: c = 3
Output: false

Example 3:

Input: c = 4
Output: true

Example 4:

Input: c = 2
Output: true

Example 5:

Input: c = 1
Output: true

 

Constraints:

    0 <= c <= 231 - 1

'''
#tle
# class Solution:
#     def judgeSquareSum(self, c: int) -> bool:
#         return bool([(i, j) for i in range(c+1) for j in range(c+1) if i*i + j*j == c])

# class Solution:
    # def judgeSquareSum(self, c: int) -> bool:
    #     squares = []
    #     for i in range(int(c**.5)+1):
    #         squares.append(i*i)
    #     print(squares)
    #     beg, end = 0, len(squares)-1
    #     while beg <= end:
    #         if squares[beg] + squares[end] > c:
    #             end -= 1
    #         elif squares[beg] + squares[end] < c:
    #             beg += 1
    #         else:
    #             return True
    #     return False

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        first, last = 0, c**.5
        while first <= last:
            if first*first + last*last > c:
                last -= 1
            elif first*first + last*last < c:
                first += 1
            else:
                return True
        return False
c = 5
# Output: true

# c = 3
# # Output: false

# c = 4
# # Output: true

# c = 2
# # Output: true

# c = 1
# # Output: true

c = 100

c = 2147483647

sol = Solution()
print(sol.judgeSquareSum(c))
