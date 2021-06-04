'''
Search for a Range

Solution
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109
'''
# my try
class Solution:
    def searchRange(self, nums: [int], target: int) -> [int]:
        l, r = 0, len(nums)-1
        while l<r:
            mid = l +((r-l)>>1)
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                if mid != 0:
                    l = mid - (mid//2)
                    r = mid + (mid//2)
                if l < 0: l = 0
                if r >= len(nums): r = len(nums)-1
                while nums[l] == target:
                    if mid > 1:
                        l -= (mid//2)
                    else:
                        l -= 1
                    if l<=0:
                        l = 0
                        break
                while nums[l] != target:
                    l += 1
                while nums[r] == target:
                    if mid > 1:
                        r += (mid//2)
                    else:
                        r += 1
                    if r>=len(nums)-1:
                        r = len(nums)-1
                        break
                while nums[r] != target:
                    r -= 1
                break
        if l == r:
            if nums[l] == target:
                return [l, l]
            else:
                return [-1, -1]
        if l > r:
            return [-1, -1]
        return [l, r]

'''
Clean iterative solution with two binary searches (with explanation)
131.3K
VIEWS
852
Last Edit: October 24, 2018 11:48 AM

stellari
stellari
 4149
The problem can be simply broken down as two binary searches for the begining and end of the range, respectively:

First let's find the left boundary of the range. We initialize the range to [i=0, j=n-1]. In each step, calculate the middle element [mid = (i+j)/2]. Now according to the relative value of A[mid] to target, there are three possibilities:

If A[mid] < target, then the range must begins on the right of mid (hence i = mid+1 for the next iteration)
If A[mid] > target, it means the range must begins on the left of mid (j = mid-1)
If A[mid] = target, then the range must begins on the left of or at mid (j= mid)
Since we would move the search range to the same side for case 2 and 3, we might as well merge them as one single case so that less code is needed:

2*. If A[mid] >= target, j = mid;

Surprisingly, 1 and 2* are the only logic you need to put in loop while (i < j). When the while loop terminates, the value of i/j is where the start of the range is. Why?

No matter what the sequence originally is, as we narrow down the search range, eventually we will be at a situation where there are only two elements in the search range. Suppose our target is 5, then we have only 7 possible cases:

case 1: [5 7] (A[i] = target < A[j])
case 2: [5 3] (A[i] = target > A[j])
case 3: [5 5] (A[i] = target = A[j])
case 4: [3 5] (A[j] = target > A[i])
case 5: [3 7] (A[i] < target < A[j])
case 6: [3 4] (A[i] < A[j] < target)
case 7: [6 7] (target < A[i] < A[j])
For case 1, 2 and 3, if we follow the above rule, since mid = i => A[mid] = target in these cases, then we would set j = mid. Now the loop terminates and i and j both point to the first 5.

For case 4, since A[mid] < target, then set i = mid+1. The loop terminates and both i and j point to 5.

For all other cases, by the time the loop terminates, A[i] is not equal to 5. So we can easily know 5 is not in the sequence if the comparison fails.

In conclusion, when the loop terminates, if A[i]==target, then i is the left boundary of the range; otherwise, just return -1;

For the right of the range, we can use a similar idea. Again we can come up with several rules:

If A[mid] > target, then the range must begins on the left of mid (j = mid-1)
If A[mid] < target, then the range must begins on the right of mid (hence i = mid+1 for the next iteration)
If A[mid] = target, then the range must begins on the right of or at mid (i= mid)
Again, we can merge condition 2 and 3 into:

2* If A[mid] <= target, then i = mid;
However, the terminate condition on longer works this time. Consider the following case:

[5 7], target = 5
Now A[mid] = 5, then according to rule 2, we set i = mid. This practically does nothing because i is already equal to mid. As a result, the search range is not moved at all!

The solution is by using a small trick: instead of calculating mid as mid = (i+j)/2, we now do:

mid = (i+j)/2+1
Why does this trick work? When we use mid = (i+j)/2, the mid is rounded to the lowest integer. In other words, mid is always biased towards the left. This means we could have i == mid when j - i == mid, but we NEVER have j == mid. So in order to keep the search range moving, you must make sure the new i is set to something different than mid, otherwise we are at the risk that i gets stuck. But for the new j, it is okay if we set it to mid, since it was not equal to mid anyways. Our two rules in search of the left boundary happen to satisfy these requirements, so it works perfectly in that situation. Similarly, when we search for the right boundary, we must make sure i won't get stuck when we set the new i to i = mid. The easiest way to achieve this is by making mid biased to the right, i.e. mid = (i+j)/2+1.

All this reasoning boils down to the following simple code:

vector<int> searchRange(int A[], int n, int target) {
    int i = 0, j = n - 1;
    vector<int> ret(2, -1);
    // Search for the left one
    while (i < j)
    {
        int mid = (i + j) /2;
        if (A[mid] < target) i = mid + 1;
        else j = mid;
    }
    if (A[i]!=target) return ret;
    else ret[0] = i;
    
    // Search for the right one
    j = n-1;  // We don't have to set i to 0 the second time.
    while (i < j)
    {
        int mid = (i + j) /2 + 1;   // Make mid biased to the right
        if (A[mid] > target) j = mid - 1;  
        else i = mid;               // So that this won't make the search range stuck.
    }
    ret[1] = j;
    return ret; 
}
'''

#from leetcode, two binary search
def searchRange(self, nums, target):
    def binarySearchLeft(A, x):
        left, right = 0, len(A) - 1
        while left <= right:
            mid = (left + right) / 2
            if x > A[mid]: left = mid + 1
            else: right = mid - 1
        return left

    def binarySearchRight(A, x):
        left, right = 0, len(A) - 1
        while left <= right:
            mid = (left + right) / 2
            if x >= A[mid]: left = mid + 1
            else: right = mid - 1
        return right
        
    left, right = binarySearchLeft(nums, target), binarySearchRight(nums, target)
    return (left, right) if left <= right else [-1, -1]

#from leetcode, two binary search by stefan
def searchRange(self, nums, target):
    def search(n):
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = (lo + hi) / 2
            if nums[mid] >= n:
                hi = mid
            else:
                lo = mid + 1
        return lo
    lo = search(target)
    return [lo, search(target+1)-1] if target in nums[lo:lo+1] else [-1, -1]

# using library
def searchRange(self, nums, target):
    lo = bisect.bisect_left(nums, target)
    return [lo, bisect.bisect(nums, target)-1] if target in nums[lo:lo+1] else [-1, -1]

#using divide and conquer
def searchRange(self, nums, target):
    def search(lo, hi):
        if nums[lo] == target == nums[hi]:
            return [lo, hi]
        if nums[lo] <= target <= nums[hi]:
            mid = (lo + hi) / 2
            l, r = search(lo, mid), search(mid+1, hi)
            return max(l, r) if -1 in l+r else [l[0], r[1]]
        return [-1, -1]
    return search(0, len(nums)-1)

nums = [5,7,7,8,8,10]
target = 8
# Output: [3,4]
nums = [5,7,7,8,8,10]
target = 6
# Output: [-1,-1]
nums = []
target = 0
# Output: [-1,-1]
# nums = [2,2]
# target = 1
# Output: [-1,-1]
nums = [2,2]
target = 2
# Output: [0, 1]
nums = [1,2,3]
target = 2
#Output: [1, 1]
nums = [0,0,1,2,2]
target = 0
#Output: [0, 1]
s = Solution()
print(s.searchRange(nums, target))
