'''
Three Equal Parts
You are given an array arr which consists of only zeros and ones, divide the array into three non-empty parts such that all of these parts represent the same binary value.

If it is possible, return any [i, j] with i + 1 < j, such that:

arr[0], arr[1], ..., arr[i] is the first part,
arr[i + 1], arr[i + 2], ..., arr[j - 1] is the second part, and
arr[j], arr[j + 1], ..., arr[arr.length - 1] is the third part.
All three parts have equal binary values.
If it is not possible, return [-1, -1].

Note that the entire part is used when considering what binary value it represents. For example, [1,1,0] represents 6 in decimal, not 3. Also, leading zeros are allowed, so [0,1,1] and [1,1] represent the same value.

 

Example 1:

Input: arr = [1,0,1,0,1]
Output: [0,3]
Example 2:

Input: arr = [1,1,0,1,1]
Output: [-1,-1]
Example 3:

Input: arr = [1,1,0,0,1]
Output: [0,2]
 

Constraints:

3 <= arr.length <= 3 * 104
arr[i] is 0 or 1
'''

class Solution:
    def threeEqualParts(self, arr: [int]) -> [int]:
        num_ones = sum(arr)
        
        if num_ones == 0:
            return [0, 2]
        
        if num_ones % 3 != 0:
            return [-1, -1]
        
        c = 0
        s1 = s2 = s3 = -1
        for idx,x in enumerate(arr):
            if x == 1:
                c += 1
            
            if c == 1 and s1 < 0:
                s1 = idx
                
            if c == num_ones//3 + 1 and s2 < 0:
                s2 = idx
                
            if c == num_ones*2//3 + 1 and s3 < 0:
                s3 = idx
                break
                
        n = len(arr[s3:]) # The length of each part when all the leading 0's are removed
        
        if arr[s1:s1+n] == arr[s2:s2+n] and arr[s2:s2+n] == arr[s3:]:
            return [s1+n-1, s2+n]
        else:
            return [-1, -1]

arr = [1,0,1,0,1]
# Output: [0,3]

sol = Solution()
print(sol.threeEqualParts(arr))
