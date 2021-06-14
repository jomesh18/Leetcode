'''
Two Sum II - Input array is sorted

Solution
Given an array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number.

Return the indices of the two numbers (1-indexed) as an integer array answer of size 2, where 1 <= answer[0] < answer[1] <= numbers.length.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

 

Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
Example 2:

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Example 3:

Input: numbers = [-1,0], target = -1
Output: [1,2]
 

Constraints:

2 <= numbers.length <= 3 * 104
-1000 <= numbers[i] <= 1000
numbers is sorted in non-decreasing order.
-1000 <= target <= 1000
The tests are generated such that there is exactly one solution.
'''
# O(n2) time, O(1) space
# class Solution:
#     def twoSum(self, numbers: [int], target: int) -> [int]:
#         i, j, res = 0, 1, []
#         while i < j < len(numbers):
#             if numbers[i] + numbers[j] < target:
#                 j += 1
#             elif numbers[i] + numbers[j] == target:
#                 res += i+1, j+1
#                 return res
#             else:
#                 i += 1
#                 j = i + 1

# O(nlogn) time, O(1) space
import bisect
class Solution:
    def twoSum(self, numbers: [int], target: int) -> [int]:
        for i in range(len(numbers)):
            index = bisect.bisect_left(numbers, target-numbers[i], i+1, len(numbers))
            if index < len(numbers) and numbers[i] + numbers[index] == target:
                return [i+1, index+1]

#O(n2) time, O(1) space
# class Solution:
#     def twoSum(self, numbers: [int], target: int) -> [int]:
#         for num in numbers:
#             if target-num in numbers:
#                 return [numbers.index(num)+1, numbers.index(target-num)+1]

# two-pointer, O(n) time, O(1) space
def twoSum1(self, numbers, target):
    l, r = 0, len(numbers)-1
    while l < r:
        s = numbers[l] + numbers[r]
        if s == target:
            return [l+1, r+1]
        elif s < target:
            l += 1
        else:
            r -= 1
'''
vector<int> twoSum(vector<int>& numbers, int target) {
    int lo=0, hi=numbers.size()-1;
    while (numbers[lo]+numbers[hi]!=target){
        if (numbers[lo]+numbers[hi]<target){
            lo++;
        } else {
            hi--;
        }
    }
    return vector<int>({lo+1,hi+1});
}
'''
 
# dictionary O(n) time, O(n) space
def twoSum2(self, numbers, target):
    dic = {}
    for i, num in enumerate(numbers):
        if target-num in dic:
            return [dic[target-num]+1, i+1]
        dic[num] = i

# import timeit
# def sol1_time():
#     SETUP ='''
# numbers = [2,7,11,15]
# target = 9
# s = Solution()'''
#     TEST_CODE = '''
# s.twoSum(numbers, target)'''

#     times = timeit.repeat(setup = SETUP, 
#                             stmt = TEST_CODE,
#                             repeat = 3,
#                             number = 10000)

#     # priniting minimum exec. time
#     print('First Solution time: {}'.format(min(times)))

numbers = [2,7,11,15]
target = 9
# Output: [1,2]

# numbers = [2,3,4]
# target = 6
# # # Output: [1,3]

# numbers = [-1,0]
# target = -1
# # # # Output: [1,2]

numbers = [5,25,75]
target = 100
# Output: [1, 2]

s = Solution()
print(s.twoSum(numbers, target))

# if __name__ == "__main__":
#     sol1_time()