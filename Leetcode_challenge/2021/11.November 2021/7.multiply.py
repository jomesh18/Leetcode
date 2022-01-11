'''
43. Multiply Strings
Medium

3614

1431

Add to List

Share
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

 

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"
 

Constraints:

1 <= num1.length, num2.length <= 200
num1 and num2 consist of digits only.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
Accepted
445,701
Submissions
1,211,179
'''
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        ans = 0
        for j, val2 in enumerate(num2[::-1]):
            carry = 0
            level_sum = []
            pos = 10**j
            for i, val1 in enumerate(num1[::-1]):
                temp = int(val2)*int(val1)+carry
                temp_res, carry = temp%10, temp//10
                # level_sum += 10**i*temp_res if temp_res else 10*
                level_sum.append(str(temp_res))
            level_sum.append(str(carry))
            ans += int("".join(level_sum[::-1]))*pos
        return str(ans)