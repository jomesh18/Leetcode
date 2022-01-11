'''
 Add Strings

Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.

 

Example 1:

Input: num1 = "11", num2 = "123"
Output: "134"

Example 2:

Input: num1 = "456", num2 = "77"
Output: "533"

Example 3:

Input: num1 = "0", num2 = "0"
Output: "0"

 

Constraints:

    1 <= num1.length, num2.length <= 104
    num1 and num2 consist of only digits.
    num1 and num2 don't have any leading zeros except for the zero itself.

'''

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        c = 0
        ans = []
        num1_index = len(num1) - 1
        num2_index = len(num2) - 1
        while num1_index >= 0 and num2_index >= 0:
            s = int(num1[num1_index]) + int(num2[num2_index]) + c
            c = s//10
            ans.append(s%10)
            num1_index -= 1
            num2_index -= 1
        if num1_index > num2_index:
            while num1_index >= 0:
                s = int(num1[num1_index]) + c
                c = s//10
                ans.append(s%10)
                num1_index -= 1
        else:
            while num2_index >= 0:
                s = int(num2[num2_index]) + c
                c = s//10
                ans.append(s%10)
                num2_index -= 1
        if c:
            ans.append(c)
        return "".join(str(val) for val in ans[::-1])

num1 = "11"
num2 = "123"
# Output: "134"

num1 = "456"
num2 = "77"
# Output: "533"

num1 = "0"
num2 = "0"
# Output: "0"

sol = Solution()
print(sol.addStrings(num1, num2))
