'''
4Sum II

Given four integer arrays nums1, nums2, nums3, and nums4 all of length n, return the number of tuples (i, j, k, l) such that:

    0 <= i, j, k, l < n
    nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0

 

Example 1:

Input: nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]
Output: 2
Explanation:
The two tuples are:
1. (0, 0, 0, 1) -> nums1[0] + nums2[0] + nums3[0] + nums4[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> nums1[1] + nums2[1] + nums3[0] + nums4[0] = 2 + (-1) + (-1) + 0 = 0

Example 2:

Input: nums1 = [0], nums2 = [0], nums3 = [0], nums4 = [0]
Output: 1

 

Constraints:

    n == nums1.length
    n == nums2.length
    n == nums3.length
    n == nums4.length
    1 <= n <= 200
    -228 <= nums1[i], nums2[i], nums3[i], nums4[i] <= 228

'''
class Solution:
    def fourSumCount(self, nums1: [int], nums2: [int], nums3: [int], nums4: [int]) -> int:
        count = 0
        num1_2 = {}
        for num1 in nums1:
            for num2 in nums2:
                num1_2[num1+num2] = num1_2.get(num1+num2, 0) + 1
        for num3 in nums3:
            for num4 in nums4:
                if -(num3+num4) in num1_2:
                    count += 1*num1_2[-(num3+num4)]
        return count

#leetcode, fastest
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        counter1 = Counter(nums1)
        counter2 = Counter(nums2)
        counter3 = Counter(nums3)
        counter4 = Counter(nums4)

        ans = 0

        counterA = defaultdict(int)
        for n1, cnt1 in counter1.items():
            for n2, cnt2 in counter2.items():
                counterA[n1+n2] += cnt1 * cnt2
        counterB = defaultdict(int)
        for n3, cnt3 in counter3.items():
            for n4, cnt4 in counter4.items():
                counterB[n3+n4] += cnt3 * cnt4

        for n1n2, cntA in counterA.items():
            if -n1n2 in counterB:
                ans += cntA * counterB[-n1n2]

        return ans

#stefan pochman
def fourSumCount(self, A, B, C, D):
    AB = collections.Counter(a+b for a in A for b in B)
    return sum(AB[-c-d] for c in C for d in D)


nums1 = [1,2]
nums2 = [-2,-1]
nums3 = [-1,2]
nums4 = [0,2]
# Output: 2

# nums1 = [0]
# nums2 = [0]
# nums3 = [0]
# nums4 = [0]
# # Output: 1

nums1 = [-1,-1]
nums2 = [-1,1]
nums3 = [-1,1]
nums4 = [1,-1]
#Output: 6

sol = Solution()
print(sol.fourSumCount(nums1, nums2, nums3, nums4))
