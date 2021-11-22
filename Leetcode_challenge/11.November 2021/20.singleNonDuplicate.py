'''
540. Single Element in a Sorted Array
Medium

You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.

Return the single element that appears only once.

Your solution must run in O(log n) time and O(1) space.

 

Example 1:

Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2

Example 2:

Input: nums = [3,3,7,7,10,11,11]
Output: 10

 

Constraints:

    1 <= nums.length <= 105
    0 <= nums[i] <= 105

Accepted
233,140
Submissions
399,426
'''
# Accepted, O(n) time, O(1) space
class Solution:
    def singleNonDuplicate(self, nums: [int]) -> int:
        for i in range(0, len(nums)-1, 2):
            if nums[i] != nums[i+1]:
                return nums[i]
        return nums[-1]

# Accepted, O(logn) time, O(1) space
'''
✔️ Solution - VI (Binary Search)

This approach uses the fact that since the array is sorted, every duplicate element occur adjacently. We can also see that the length of given array must be odd (Why? All element occur twice while only 1 element occurs once).

Let the search range be [L, R]. Now, when we consider the mid element, the array is split into two equal halves on the left and right sides. Then we have following cases -

    nums[mid] == nums[mid+1]:

        Left Half Length = Right Half Length = Even : In this case, we can be sure that our answer lies in the right half. How? One element of right half: nums[mid+1] matches with nums[mid]. So, leaving nums[mid+1] aside, we only have odd number of elements to pair up with each other in the right half. This means one element must be such that it cannot be paired with anyone and this is our required answer that occurs only once. So do L = mid+2 (+2 to skip nums[mid] and nums[mid+1] & keep search space odd for next iteration)
        Left Half Length = Right Half Length = Odd : In this case, we can be sure that our answer lies in the left half. Again, how? Following same reasoning, one element of left half: nums[mid+1] matches with nums[mid]. So, leaving nums[mid+1] aside, the right half consists of even number of elements which can pair up with each other completely. However, left half only consists odd elements and thus one element which cannot be paired with anyone is our required answer. So do R = mid-1 (-1 to skip nums[mid] & keep search space odd for next iteration)

    nums[mid] == nums[mid-1]: We can follow similar reasoning based on array lengths as above -

        Left Half Length = Right Half Length = Even : The answer lies in the left half. How? One element of left half: nums[mid-1] matches with nums[mid]. This leaves left half with odd number of elements to pair up with each other and one element that cant be paired with anyone is the required answer. So do R = mid-2
        Left Half Length = Right Half Length = Odd : The answer lies in right half. How? One element of left half: nums[mid-1] matches with nums[mid]. This leaves left half with even number of elements which can pair up with each other completely. However, right half only consists odd elements and thus one element which cannot be paired with any other is the required answer. So do L = mid+1.

    If neither of above condition are satisfied, then we can be sure that nums[mid] itself is the required element occuring once (since it doesnt match with its neighbours). So we can just return it.
    '''
class Solution:
    def singleNonDuplicate(self, nums: [int]) -> int:
        l, r = 0, len(nums)-1
        while l<=r:
            mid = (l+r)>>1
            half_len_odd = (mid - l) % 2
            if mid+1<n and nums[mid] == nums[mid+1]:
                if half_len_odd:
                    r = mid - 1
                else:
                    l = mid + 2
            elif mid and nums[mid] == nums[mid-1]:
                if half_len_odd:
                    l = mid + 1
                else:
                    r = mid - 2
            else:
                return nums[mid]
        return -1


'''✔️ Solution VII (Binary Search - 2nd Approach)

We can apply binary search using slightly different logic as well.

Suppose you are given a sorted array with all elements occur twice. For eg. [1,1,2,2,5,5,7,7,8,8]. So, here we can see that the elements follow the condition - nums[i] == nums[i+1], nums[i+2] == nums[i+3], nums[i+2*k] == nums[i+2*k+1]. Now, if we insert an element somewhere in the array, the above relation wont be satisfied from that point of insertion. Eg. [1,1,2,2,4,5,5,7,7,8,8] the condition starts to fail from element 4, that is from point where single-occurence element is present.

Thus, we can use this observation to apply binary-search to find the starting point from where the above condition starts to fail. This start point is the index of element occuring once. The binary search will be applied as follows -

    Initialize the search space as [L, R] = [0, n-1] and repeat the following step till L <= R.
    Find the mid position and check if the above condition nums[i+2*k] == nums[i+2*k+1] is satisifed or not.
    For this, firstly we must ensure that mid is even. If mid is odd, decrease it by 1 to make it even.
    Then, we need to check if the condition is satisfied or not -
        nums[mid] == nums[mid+1] : The condition is correctly satisfied till index mid+1. So, the required element must occur somewhere on the right of mid+1. So do L = mid+2.
        nums[mid] != nums[mid+1] : The condition is not satisfied at this point. So, the required element must either be nums[mid] or occur somewhere on the left of mid due to which the relation is not satisfied. Mark nums[mid] as a potential answer and search if condition is satisfied to the left of mid by doing R = mid-1

Finally, we return the ans which was marked as potential answer during the binary search.'''

class Solution:
    def singleNonDuplicate(self, nums: [int]) -> int:
        l, r = 0, len(nums)-1
        ans = -1
        while l <= r:
            mid = (l+r)>>1
            if mid >> 1: mid -= 1
            if mid+1<len(nums) and nums[mid] = nums[mid+1]:
                l = mid + 2
            else:
                ans = nums[mid]
                r = mid - 1
        return ans

#stefan pochman
class Solution:
    def singleNonDuplicate(self, nums):
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) / 2
            if nums[mid] == nums[mid ^ 1]:
                lo = mid + 1
            else:
                hi = mid
        return nums[lo]