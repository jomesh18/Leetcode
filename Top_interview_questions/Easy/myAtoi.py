'''
String to Integer (atoi)

Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

The algorithm for myAtoi(string s) is as follows:

    Read in and ignore any leading whitespace.
    Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
    Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.
    Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
    If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range. Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
    Return the integer as the final result.

Note:

    Only the space character ' ' is considered a whitespace character.
    Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.

 

Example 1:

Input: s = "42"
Output: 42
Explanation: The underlined characters are what is read in, the caret is the current reader position.
Step 1: "42" (no characters read because there is no leading whitespace)
         ^
Step 2: "42" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "42" ("42" is read in)
           ^
The parsed integer is 42.
Since 42 is in the range [-231, 231 - 1], the final result is 42.

Example 2:

Input: s = "   -42"
Output: -42
Explanation:
Step 1: "   -42" (leading whitespace is read and ignored)
            ^
Step 2: "   -42" ('-' is read, so the result should be negative)
             ^
Step 3: "   -42" ("42" is read in)
               ^
The parsed integer is -42.
Since -42 is in the range [-231, 231 - 1], the final result is -42.

Example 3:

Input: s = "4193 with words"
Output: 4193
Explanation:
Step 1: "4193 with words" (no characters read because there is no leading whitespace)
         ^
Step 2: "4193 with words" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "4193 with words" ("4193" is read in; reading stops because the next character is a non-digit)
             ^
The parsed integer is 4193.
Since 4193 is in the range [-231, 231 - 1], the final result is 4193.

Example 4:

Input: s = "words and 987"
Output: 0
Explanation:
Step 1: "words and 987" (no characters read because there is no leading whitespace)
         ^
Step 2: "words and 987" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "words and 987" (reading stops immediately because there is a non-digit 'w')
         ^
The parsed integer is 0 because no digits were read.
Since 0 is in the range [-231, 231 - 1], the final result is 0.

Example 5:

Input: s = "-91283472332"
Output: -2147483648
Explanation:
Step 1: "-91283472332" (no characters read because there is no leading whitespace)
         ^
Step 2: "-91283472332" ('-' is read, so the result should be negative)
          ^
Step 3: "-91283472332" ("91283472332" is read in)
                     ^
The parsed integer is -91283472332.
Since -91283472332 is less than the lower bound of the range [-231, 231 - 1], the final result is clamped to -231 = -2147483648.

 

Constraints:

    0 <= s.length <= 200
    s consists of English letters (lower-case and upper-case), digits (0-9), ' ', '+', '-', and '.'.

'''
# class Solution:
#     def myAtoi(self, s: str) -> int:
#         if len(s) == 0:
#             return 0
#         isNeg = False
#         i = 0
#         while i < len(s) and s[i] == " ":  #step 1: read and ignore leading whitespaces
#             i += 1
#         if i < len(s) and s[i] == '-': #step 2: check for sign
#             isNeg = True
#             i += 1
#         elif i < len(s) and s[i] == "+":
#             i += 1
#         start = i   #step 2: started reading digit characters
#         while i < len(s) and s[i].isnumeric():
#             i += 1
#         num = 0
#         for k in range(start, i):
#             num = num*10 + int(s[k])
#         # print(num)
#         if isNeg:
#             if num > 1<<31:
#                 num = 1<<31
#             return -num
#         if num > (1<<31)-1:
#             num = (1<<31)-1
#         return num


#using fda(finite state automation)
# class StateMachine:
#     def __init__(self):
#         self.State = { "q0": 1, "q1": 2, "q2": 3, "qd": 4 }
#         self.INT_MAX, self.INT_MIN = pow(2, 31) - 1, -pow(2, 31)
        
#         # Store current state value.
#         self.__current_state = self.State["q0"]
#         # Store result formed and its sign.
#         self.__result = 0
#         self.__sign = 1

#     def to_state_q1(self, ch: chr) -> None:
#         """Transition to state q1."""
#         self.__sign = -1 if (ch == '-') else 1
#         self.__current_state = self.State["q1"]
    
#     def to_state_q2(self, digit: int) -> None:
#         """Transition to state q2."""
#         self.__current_state = self.State["q2"]
#         self.append_digit(digit)
    
#     def to_state_qd(self) -> None:
#         """Transition to dead state qd."""
#         self.__current_state = self.State["qd"]
    
#     def append_digit(self, digit: int) -> None:
#         """Append digit to result, if out of range return clamped value."""
#         if ((self.__result > self.INT_MAX // 10) or 
#             (self.__result == self.INT_MAX // 10 and digit > self.INT_MAX % 10)):
#             if self.__sign == 1:
#                 # If sign is 1, clamp result to INT_MAX.
#                 self.__result = self.INT_MAX
#             else:
#                 # If sign is -1, clamp result to INT_MIN.
#                 self.__result = self.INT_MIN
#                 self.__sign = 1
            
#             # When the 32-bit int range is exceeded, a dead state is reached.
#             self.to_state_qd()
#         else:
#             # Append current digit to the result. 
#             self.__result = (self.__result * 10) + digit

#     def transition(self, ch: chr) -> None:
#         """Change state based on current input character."""
#         if self.__current_state == self.State["q0"]:
#             # Beginning state of the string (or some whitespaces are skipped).
#             if ch == ' ':
#                 # Current character is a whitespaces.
#                 # We stay in same state. 
#                 return
#             elif ch == '-' or ch == '+':
#                 # Current character is a sign.
#                 self.to_state_q1(ch)
#             elif ch.isdigit():
#                 # Current character is a digit.
#                 self.to_state_q2(int(ch))
#             else:
#                 # Current character is not a space/sign/digit.
#                 # Reached a dead state.
#                 self.to_state_qd()
        
#         elif self.__current_state == self.State["q1"] or self.__current_state == self.State["q2"]:
#             # Previous character was a sign or digit.
#             if ch.isdigit():
#                 # Current character is a digit.
#                 self.to_state_q2(int(ch))
#             else:
#                 # Current character is not a digit.
#                 # Reached a dead state.
#                 self.to_state_qd()
    
#     def get_integer(self) -> None:
#         """Return the final result formed with it's sign."""
#         return self.__sign * self.__result
    
#     def get_state(self) -> None:
#         """Get current state."""
#         return self.__current_state

# class Solution:
#     def myAtoi(self, input: str) -> int:
#         q = StateMachine()
        
#         for ch in input:
#             q.transition(ch)
#             if q.get_state() == q.State["qd"]:
#                 break

#         return q.get_integer()
s = "42"
# Output: 42

s = "   -42"
# Output: -42

s = "4193 with words"
# Output: 4193

s = "words and 987"
# Output: 0

# s = "-91283472332"
# Output: -2147483648

# s = "+1"
# Output: 1

# s = "21474836460"
# Output: 2147483647

# s = " "
# Output: 0

sol = Solution()
print(sol.myAtoi(s))
