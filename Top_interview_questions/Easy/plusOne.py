'''
Plus One

You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

 

Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].

Example 2:

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].

Example 3:

Input: digits = [0]
Output: [1]
Explanation: The array represents the integer 0.
Incrementing by one gives 0 + 1 = 1.
Thus, the result should be [1].

Example 4:

Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].

 

Constraints:

    1 <= digits.length <= 100
    0 <= digits[i] <= 9
    digits does not contain any leading 0's.

'''
# recursive
class Solution:
    def plusOne(self, digits: [int]) -> [int]:
        res = []
        def helper(i, carry):
            if i < 0: 
                if carry:
                    res.append(1)
                return
            digit = digits[i]
            digit += carry
            if digit == 10:
                res.append(0)
                helper(i-1, 1)
            else:
                res.append(digit)
                helper(i-1, 0)
        
        helper(len(digits)-1, 1)
        return res[::-1]

#leetcode fastest
class Solution:
    def plusOne(self, digits: [int]) -> [int]:
        i = len(digits) - 1
        while True:
            if i == -1:
                digits.insert(0, 1)
                return digits
            elif digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                break
            i -= 1
        return digits


#2nd fastest
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(1,len(digits)+1):
            if digits[-1*i] !=9:
                digits[-1*i] +=1
                return digits

            else:
                digits[-1*i] = 0
           
        digits.insert(0,1)
     
        return digits

        
digits = [1,2,3]
# Output: [1,2,4]

digits = [4,3,2,1]
# # Output: [4,3,2,2]

digits = [0]
# # Output: [1]

digits = [9]
# Output: [1,0]

sol = Solution()
print(sol.plusOne(digits))
