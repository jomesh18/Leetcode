'''
Beautiful Array

For some fixed n, an array nums is beautiful if it is a permutation of the integers 1, 2, ..., n, such that:

For every i < j, there is no k with i < k < j such that nums[k] * 2 = nums[i] + nums[j].

Given n, return any beautiful array nums.  (It is guaranteed that one exists.)

 

Example 1:

Input: n = 4
Output: [2,1,4,3]

Example 2:

Input: n = 5
Output: [3,1,2,5,4]

 

Note:

    1 <= n <= 1000

'''
class Solution:
    def beautifulArray(self, n: int) -> [int]:
        res = [1]
        while len(res) < n:
            res = [i * 2 - 1 for i in res] + [i * 2 for i in res]
        return [i for i in res if i <= n]

def check_beautifulArray(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1, i+1, -1):
            for k in range(i+1, j):
                # print(i, j, k)
                if arr[k] *2 == arr[i] + arr[j]:
                    return False
    return True

# arr = [2, 1, 4, 3]
# arr = [3, 1, 2, 5, 4]
# arr = [3, 1, 2, 5, 6, 4]
# arr = [1, 2, 3, 4, 5]
# print(check_beautifulArray(arr))

n = 10
sol = Solution()
print(sol.beautifulArray(n))
