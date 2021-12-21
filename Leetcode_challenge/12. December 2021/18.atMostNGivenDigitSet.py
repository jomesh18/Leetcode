'''
902. Numbers At Most N Given Digit Set
Hard

650

73

Add to List

Share
Given an array of digits which is sorted in non-decreasing order. You can write numbers using each digits[i] as many times as we want. For example, if digits = ['1','3','5'], we may write numbers such as '13', '551', and '1351315'.

Return the number of positive integers that can be generated that are less than or equal to a given integer n.

 

Example 1:

Input: digits = ["1","3","5","7"], n = 100
Output: 20
Explanation: 
The 20 numbers that can be written are:
1, 3, 5, 7, 11, 13, 15, 17, 31, 33, 35, 37, 51, 53, 55, 57, 71, 73, 75, 77.
Example 2:

Input: digits = ["1","4","9"], n = 1000000000
Output: 29523
Explanation: 
We can write 3 one digit numbers, 9 two digit numbers, 27 three digit numbers,
81 four digit numbers, 243 five digit numbers, 729 six digit numbers,
2187 seven digit numbers, 6561 eight digit numbers, and 19683 nine digit numbers.
In total, this is 29523 integers that can be written using the digits array.
Example 3:

Input: digits = ["7"], n = 8
Output: 1
 

Constraints:

1 <= digits.length <= 9
digits[i].length == 1
digits[i] is a digit from '1' to '9'.
All the values in digits are unique.
digits is sorted in non-decreasing order.
1 <= n <= 109
Accepted
23,637
Submissions
63,561
'''

#tle
# class Solution:
#     def atMostNGivenDigitSet(self, digits: [str], n: int) -> int:
#         # self.ans = []
#         self.count = 0
#         d = {}
#         def helper(i, temp=0):
#             for i in range(len(digits)):
#                 temp1 = temp*10 + int(digits[i])
#                 if temp1 > n: break
#                 # self.ans.append(temp1)
#                 self.count += 1
#                 # print(self.ans, self.count)
#                 helper(i, temp1)

#         helper(0)
#         return self.count

# math solution
# class Solution:
#     def atMostNGivenDigitSet(self, digits: [str], n: int) -> int:
#         s, N, M = str(n), len(str(n)), len(digits)
#         count = sum((M**i for i in range(1, N)))
#         for i in range(N):
#             j = 0
#             while j < M and digits[j][0] < s[i]:
#                 count += M**(N-1-i)
#                 j += 1
#             if j >= M or digits[j][0] != s[i]: return count
#         return count + 1

# #above, my try
# class Solution:
#     def atMostNGivenDigitSet(self, digits: [str], n: int) -> int:
#         n_len = len(str(n))
#         no_of_digits = len(digits)
#         count = sum(no_of_digits**i for i in range(1, n_len))
#         #finding the valid counts from msb of n onwards
#         for i in range(n_len):
#             curr_dig = int(str(n)[i])
#             j = 0
#             while j < no_of_digits and curr_dig > int(digits[j]):
#                 count += no_of_digits**(n_len-i-1)
#                 j += 1
#             if j < no_of_digits and curr_dig < int(digits[j]):
#                 return count
#         return count+1


#dp+math
# class Solution:
#     def atMostNGivenDigitSet(self, digits: [str], n: int) -> int:
#         s = str(n)
#         l = len(s)
#         dig_len = len(digits)
#         dp = [0]*l+[1]

#         for i in range(l-1, -1, -1):
#             for d in digits:
#                 if d < s[i]:
#                     dp[i] += dig_len**(l-1-i)
#                 elif d == s[i]:
#                     dp[i] += dp[i+1]
#                 else:
#                     break

#         return dp[0] + sum(dig_len**i for i in range(1, l))


# Theory: https://codeforces.com/blog/entry/53960
class Solution:
    def atMostNGivenDigitSet(self, D: [str], N: int) -> int:
        D = list(map(int, D))
        N = list(map(int, str(N)))

        dic = {}
        def dp(i, isPrefix, isBigger):
            if i == len(N):
                return not isBigger
            if (i, isPrefix, isBigger) in dic: return dic[(i, isPrefix, isBigger)]
            if not isPrefix and not isBigger:
                ans = 1 + len(D) * dp(i + 1, False, False)
                dic[(i, isPrefix, isBigger)] = ans
                return ans

            ans = 1 + sum(dp(i + 1, isPrefix and d == N[i], isBigger or (isPrefix and d > N[i])) for d in D)
            dic[(i, isPrefix, isBigger)] = ans
            return ans

        return dp(0, True, False) - 1

digits = ["1","3"]
n = 100
# # Output: 6

# digits = ["1","3","5","7"]
# n = 100
# # # Output: 20

# digits = ["1","3","5","7"]
# n = 156
# # # Output: 31

# digits = ["1","3","5"]
# n = 137
# # # Output: 18

digits = ["1","3","5"]
n = 135
# Output: 18

# digits = ["1","4","9"]
# n = 1000000000
# # # Output: 29523

# digits = ["7"]
# n = 8
# # # Output: 1

# digits = [str(i) for i in range(1, 10)]
# n = 10**9
# # Output = 435848049

sol = Solution()
print(sol.atMostNGivenDigitSet(digits, n))
