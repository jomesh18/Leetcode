'''
952. Largest Component Size by Common Factor
Hard

You are given an integer array of unique positive integers nums. Consider the following graph:

    There are nums.length nodes, labeled nums[0] to nums[nums.length - 1],
    There is an undirected edge between nums[i] and nums[j] if nums[i] and nums[j] share a common factor greater than 1.

Return the size of the largest connected component in the graph.

 

Example 1:

Input: nums = [4,6,15,35]
Output: 4

Example 2:

Input: nums = [20,50,9,63]
Output: 2

Example 3:

Input: nums = [2,3,6,7,4,12,21,39]
Output: 8

 

Constraints:

    1 <= nums.length <= 2 * 104
    1 <= nums[i] <= 105
    All the values of nums are unique.

Accepted
33,546
Submissions
86,747
'''

#from leetcode, babichev
from collections import defaultdict, Counter
class DSU:
    def __init__(self, N):
        self.p = list(range(N))

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        self.p[xr] = yr

class Solution:
    def primes_set(self,n):
        for i in range(2, int(n**.5)+1):
            if n % i == 0:
                return self.primes_set(n//i) | set([i])
        return set([n])

    def largestComponentSize(self, nums: [int]) -> int:
        n = len(nums)
        UF = DSU(n)
        primes = defaultdict(list)
        for i, num in enumerate(nums):
            pr_set = self.primes_set(num)
            print(pr_set)
            for q in pr_set: primes[q].append(i)

        for _, indexes in primes.items():
            for i in range(len(indexes)-1):
                UF.union(indexes[i], indexes[i+1])

        return max(Counter([UF.find(i) for i in range(n)]).values())




# #above solution, my try
# from collections import Counter, defaultdict

class DSU:
    def __init__(self, n):
        self.parents = list(range(n))

    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        parent_x, parent_y = self.find(x), self.find(y)
        self.parents[parent_x] = parent_y

class Solution:
    def prime_factors(self, num):
        for i in range(2, int(num**.5)+1):
            if num % i == 0:
                return self.prime_factors(num//i) | set([i])
        return set([num])

    def largestComponentSize(self, nums: [int]) -> int:
        UF = DSU(len(nums))
        primes = defaultdict(list)
        for i, num in enumerate(nums):
            prime_set = self.prime_factors(num)
            print(prime_set)
            for elem in prime_set: primes[elem].append(i)
        for _, indexes in primes.items():
            for i in range(len(indexes)-1):
                UF.union(indexes[i], indexes[i+1])
        return max(Counter([UF.find(i) for i in range(len(nums))]).values())


nums = [4,6,15,35]
# Output: 4

nums = [20,50,9,63]
# # Output: 2

nums = [2,3,6,7,4,12,21,39]
# # Output: 8

nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]

sol = Solution()
print(sol.largestComponentSize(nums))
