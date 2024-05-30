'''
1442. Count Triplets That Can Form Two Arrays of Equal XOR
Medium

1539

86

Add to List

Share
Given an array of integers arr.

We want to select three indices i, j and k where (0 <= i < j <= k < arr.length).

Let's define a and b as follows:

a = arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1]
b = arr[j] ^ arr[j + 1] ^ ... ^ arr[k]
Note that ^ denotes the bitwise-xor operation.

Return the number of triplets (i, j and k) Where a == b.

 

Example 1:

Input: arr = [2,3,1,6,7]
Output: 4
Explanation: The triplets are (0,1,2), (0,2,2), (2,3,4) and (2,4,4)
Example 2:

Input: arr = [1,1,1,1,1]
Output: 10
 

Constraints:

1 <= arr.length <= 300
1 <= arr[i] <= 108
'''
# O(n*n*n)
class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        ans = 0
        n = len(arr)
        count = 0
        for i in range(n-1):
            a = 0
            for j in range(i+1, n):
                a ^= arr[j-1]
                b = 0
                for k in range(j, n):
                    b ^= arr[k]
                    if a == b:
                        count += 1
        return count


# O(n*n)
class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        prefix_xor = [0] + arr
        size = len(prefix_xor)
        count = 0
        for i in range(1, size):
            prefix_xor[i] ^= prefix_xor[i-1]
        for start in range(size-1):
            for end in range(start+1, size):
                if prefix_xor[start] == prefix_xor[end]:
                    count += end-start-1
        return count

