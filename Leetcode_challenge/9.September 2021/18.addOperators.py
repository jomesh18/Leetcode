'''
Expression Add Operators

Given a string num that contains only digits and an integer target, return all possibilities to add the binary operators '+', '-', or '*' between the digits of num so that the resultant expression evaluates to the target value.

 

Example 1:

Input: num = "123", target = 6
Output: ["1*2*3","1+2+3"]

Example 2:

Input: num = "232", target = 8
Output: ["2*3+2","2+3*2"]

Example 3:

Input: num = "105", target = 5
Output: ["1*0+5","10-5"]

Example 4:

Input: num = "00", target = 0
Output: ["0*0","0+0","0-0"]

Example 5:

Input: num = "3456237490", target = 9191
Output: []

 

Constraints:

    1 <= num.length <= 10
    num consists of only digits.
    -231 <= target <= 231 - 1

'''
class Solution:
    def addOperators(self, num: str, target: int) -> [str]:
        N = len(num)
        answers = []
        def recurse(index, prev_operand, current_operand, value, string):

            # Done processing all the digits in num
            if index == N:

                # If the final value == target expected AND
                # no operand is left unprocessed
                if value == target and current_operand == 0:
                    answers.append("".join(string[1:]))
                return

            # Extending the current operand by one digit
            current_operand = current_operand*10 + int(num[index])
            str_op = str(current_operand)

            # To avoid cases where we have 1 + 05 or 1 * 05 since 05 won't be a
            # valid operand. Hence this check
            if current_operand > 0:

                # NO OP recursion
                recurse(index + 1, prev_operand, current_operand, value, string)

            # ADDITION
            string.append('+'); string.append(str_op)
            recurse(index + 1, current_operand, 0, value + current_operand, string)
            string.pop();string.pop()

            # Can subtract or multiply only if there are some previous operands
            if string:

                # SUBTRACTION
                string.append('-'); string.append(str_op)
                recurse(index + 1, -current_operand, 0, value - current_operand, string)
                string.pop();string.pop()

                # MULTIPLICATION
                string.append('*'); string.append(str_op)
                recurse(index + 1, current_operand * prev_operand, 0, value - prev_operand + (current_operand * prev_operand), string)
                string.pop();string.pop()
        recurse(0, 0, 0, 0, [])    
        return answers

num = "123"
target = 6
# # Output: ["1*2*3","1+2+3"]

num = "232"
target = 8
# # Output: ["2*3+2","2+3*2"]

# num = "105"
# target = 5
# # Output: ["1*0+5","10-5"]

# num = "00"
# target = 0
# # Output: ["0*0","0+0","0-0"]

# num = "3456237490"
# target = 9191
# # Output: []

sol = Solution()
print(sol.addOperators(num, target))
