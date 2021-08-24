'''
Complex Number Multiplication

A complex number can be represented as a string on the form "real+imaginaryi" where:

    real is the real part and is an integer in the range [-100, 100].
    imaginary is the imaginary part and is an integer in the range [-100, 100].
    i2 == -1.

Given two complex numbers num1 and num2 as strings, return a string of the complex number that represents their multiplications.

 

Example 1:

Input: num1 = "1+1i", num2 = "1+1i"
Output: "0+2i"
Explanation: (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i, and you need convert it to the form of 0+2i.

Example 2:

Input: num1 = "1+-1i", num2 = "1+-1i"
Output: "0+-2i"
Explanation: (1 - i) * (1 - i) = 1 + i2 - 2 * i = -2i, and you need convert it to the form of 0+-2i.

 

Constraints:

    num1 and num2 are valid complex numbers.

'''
class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        real = []
        imag = []
        for n in (num1, num2):
            if "+" or "-" in n:
                if "+" in n:
                    num = n.split("+")
                else:
                    num = n.split("-")
                real.append(int(num[0]))
                imag.append(int(num[1][:-1]))
            elif "i" in n:
                real.append(0)
                imag.append(int(n[:-1]))
            else:
                real.append(int(n))
                imag.append(0)
        # print(real, imag)
        a, b, c, d = real[0], imag[0], real[1], imag[1]
        res = ""
        real_res = a*c - b*d
        imag_res = a*d + b*c
        if real_res == 0:
            res += "0+"
        else:
            res += str(real_res)+"+"
        res += str(imag_res)+"i"
        
        return res

num1 = "1+1i"
num2 = "1+1i"
# Output: "0+2i"
# # Explanation: (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i, and you need convert it to the form of 0+2i.

# num1 = "1+-1i"
# num2 = "1+-1i"
# # Output: "0+-2i"

sol = Solution()
print(sol.complexNumberMultiply(num1, num2))
