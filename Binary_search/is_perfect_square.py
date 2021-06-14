'''
 Valid Perfect Square

Solution
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Follow up: Do not use any built-in library function such as sqrt.

 

Example 1:

Input: num = 16
Output: true
Example 2:

Input: num = 14
Output: false
 

Constraints:

1 <= num <= 2^31 - 1
'''
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
    	if num == 1: return True
        l, h = 0, num>>1
        while l<h:
        	mid = l + ((h-l)>>1)
        	if mid*mid>num:
        		h = mid - 1
        	elif mid*mid<num:
        		l = mid + 1
        	else:
        		return True
        return True if l*l == num else False

# from leetcode binary search solution
class Solution:
    def BinarySearch(self, num):
        left = 0
        right = num
        
        while left <= right:
            mid = left + (right-left)//2
            if  mid ** 2 == num:
                return True
            elif mid ** 2 > num:
                right = mid -1
            else:
                left = mid +1
        return False

#from leetcode, math solution
'''
Addition of first n odd numbers is always perfect square 
1 + 3 = 4,      
1 + 3 + 5 = 9,     
1 + 3 + 5 + 7 + 9 + 11 = 36 ...
1 + 3 + 5 + ...  (2n-1) = ∑(2*i - 1) where 1<=i<=n
                        = 2*∑i - ∑1  where 1<=i<=n
                        = 2n(n+1)/2 - n
                        = n(n+1) - n
                        = n**n
                        '''
class Solution:
	def Math(self, num):
	        i = 1
	        while (num>0):
	            num -= i
	            i += 2       
	        return num == 0

# Newtons method
class Solution:
    def NewtonMethod(self, num):
	    r = num
	    while r*r > num:
	        r = (r + num/r) // 2
	    return r*r == num	        

# bitwise trick solution, not understood
class Solution:
    def BitwiseTrick(self, num):
       root = 0
       bit = 1 << 15
       
       while bit > 0 :
           root |= bit
           if root > num // root:    
               root ^= bit                
           bit >>= 1        
       return root * root == num


num = 16
# Output: true
num = 15
# Output: false
s = Solution()
for num in range(50):
	ans = s.isPerfectSquare(num)
	if ans:
		print(num, ans)
