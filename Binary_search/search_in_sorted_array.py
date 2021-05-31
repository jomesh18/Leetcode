'''
Search in Rotated Sorted Array

Solution
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1
 

Constraints:

1 <= nums.length <= 5000
-104 <= nums[i] <= 104
All values of nums are unique.
nums is guaranteed to be rotated at some pivot.
-104 <= target <= 104
'''

'''another idea, find the lowest value in nums by binary search
then find the target
class Solution {
public:
    int search(int A[], int n, int target) {
        int lo=0,hi=n-1;
        // find the index of the smallest value using binary search.
        // Loop will terminate since mid < hi, and lo or hi will shrink by at least 1.
        // Proof by contradiction that mid < hi: if mid==hi, then lo==hi and loop would have been terminated.
        while(lo<hi){
            int mid=(lo+hi)/2;
            if(A[mid]>A[hi]) lo=mid+1;
            else hi=mid;
        }
        // lo==hi is the index of the smallest value and also the number of places rotated.
        int rot=lo;
        lo=0;hi=n-1;
        // The usual binary search and accounting for rotation.
        while(lo<=hi){
            int mid=(lo+hi)/2;
            int realmid=(mid+rot)%n;
            if(A[realmid]==target)return realmid;
            if(A[realmid]<target)lo=mid+1;
            else hi=mid-1;
        }
        return -1;
    }
};
'''

#my try, find pivot, the do search on both sides of pivot
# class Solution:
#     def search(self, nums: [int], target: int) -> int:
        
#         def binary_search(nums, target):
#             l, r = 0, len(nums)
#             while l < r:
#                 mid = l+((r-l)>>1)
#                 if nums[mid] == target:
#                     return mid
#                 if nums[mid] > target:
#                     r = mid
#                 else:
#                     l = mid + 1
#             return -1

#         l = len(nums)
#         if l == 1 or l == 2:
#             if nums[0] == target:
#                 return 0
#             elif l == 2 and nums[1] == target:
#                 return 1
#             else:
#                 return -1
             
#         def find_pivot(nums):
#             l, r = 0, len(nums)-1
#             if nums[l] < nums[r]:
#                 return -1
#             while True:
#                 mid = l+((r-l)>>1)
#                 if nums[l] < nums[mid]:
#                     l = mid
#                 elif nums[mid]< nums[r]:
#                     r = mid
#                 else:
#                     return mid

#         pivot = find_pivot(nums)
#         if pivot == -1:
#             return binary_search(nums, target)
#         else:
#             ans1 = binary_search(nums[:pivot+1], target)
#             ans2 = binary_search(nums[pivot+1:], target)

#             if ans1 != -1:
#                 return ans1
#             elif ans2 != -1:
#                 return pivot+1+ans2
#             else:
#                 return -1


#from leetcode

class Solution:
    def search(self, nums, target):
        if not nums:
            return -1

        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) / 2
            if target == nums[mid]:
                return mid

            if nums[low] <= nums[mid]:
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return -1

#from leetcode
'''The most important observation is the "If nums[mid] and target are "on the same side" of nums[0], just take nums[mid]".'''
class Solution:
    def search(self, nums, target):
            lo, hi = 0, len(nums)

            while lo < hi:
                mid = (lo + hi) // 2
                
                if (nums[mid] < nums[0]) == ( target < nums[0]):
                    if (nums[mid] < target):
                        lo = mid + 1
                    elif (nums[mid] > target):
                        hi = mid
                    else:
                        return mid
                elif target < nums[0]:
                    lo = mid + 1
                else:
                    hi = mid

            return -1


#from leetcode, stefan
'''
Explanation
My solutions use binary search guided by the following thoughts:

Remember the array is sorted, except it might drop at one point.

If nums[0] <= nums[i], then nums[0..i] is sorted (in case of "==" it's just one element, and in case of "<" there must be a drop elsewhere). So we should keep searching in nums[0..i] if the target lies in this sorted range, i.e., if nums[0] <= target <= nums[i].

If nums[i] < nums[0], then nums[0..i] contains a drop, and thus nums[i+1..end] is sorted and lies strictly between nums[i] and nums[0]. So we should keep searching in nums[0..i] if the target doesn't lie strictly between them, i.e., if target <= nums[i] < nums[0] or nums[i] < nums[0] <= target

Those three cases look cyclic:

    nums[0] <= target <= nums[i]
               target <= nums[i] < nums[0]
                         nums[i] < nums[0] <= target
So I have the three checks (nums[0] <= target), (target <= nums[i]) and (nums[i] < nums[0]), and I want to know whether exactly two of them are true. They can't all be true or all be false (check it), so I just need to distinguish between "two true" and "one true". Parity is enough for that, so instead of adding them I xor them, which is a bit shorter and particularly helpful in Java and Ruby, because those don't let me add booleans but do let me xor them.

(Actually while developing this I thought of permutations of nums[0], target and nums[i] and the permutation parity and saw those three checks as representing inversions, but I had trouble putting that into words and now find the above explanation much better. But it helped me get there, so I wanted to mention it here.)
'''
class Solution:
    def search(self, nums, target):
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) / 2
            if (nums[0] > target) ^ (nums[0] > nums[mid]) ^ (target > nums[mid]):
                lo = mid + 1
            else:
                hi = mid
        return lo if target in nums[lo:lo+1] else -1

# nums = [4,5,6,7,0,1,2]
# target = 0
# # Output: 4

# nums = [4,5,6,7,0,1,2]
# target = 3
# Output: -1

# nums = [1]
# target = 0
# Output: -1

# nums = [1,3]
# target = 0
# # Output: -1

# nums = [3,1]
# target = 3
# # Output: 0

# nums = [1]
# target = 0
# # Output = -1

# nums = [1,3,5]
# target = 0
# Output = -1

# nums = [1,3,5]
# target = 1
# Output = 0

nums = [5,1,3]
target = 0
# Output = -1

nums = [5,1,3]
target = 5
# Output = 0

nums = [1]
target = 1

# nums = [7,8,1,2,3,4,5,6]
# target = 2
#Output = 3

s = Solution()
print(s.search(nums, target))
