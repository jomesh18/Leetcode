'''
315. Count of Smaller Numbers After Self
Hard

7194

200

Add to List

Share
You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

 

Example 1:

Input: nums = [5,2,6,1]
Output: [2,1,1,0]
Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.
Example 2:

Input: nums = [-1]
Output: [0]
Example 3:

Input: nums = [-1,-1]
Output: [0,0]
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
Accepted
269,011
Submissions
627,089
'''
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        arr = [(num, i) for i, num in enumerate(nums)]
        res = [0]*len(nums)
        
        def merge(l, mid, r):
            out = []
            i = l
            j = mid+1
            rightlessthanleft = 0
            while i < mid+1 and j <= r:
                if arr[i][0] > arr[j][0]:
                    out.append(arr[j])
                    j += 1
                    rightlessthanleft += 1
                else:
                    out.append(arr[i])
                    res[arr[i][1]] += rightlessthanleft
                    i += 1
            while i < mid + 1:
                out.append(arr[i])
                res[arr[i][1]] += rightlessthanleft
                i += 1
            while j <= r:
                out.append(arr[j])
                j += 1
            for i in range(l, r+1):
                arr[i] = out[i-l]
            
        def merge_sort(l, r):
            if l < r:
                mid = (l+r)//2
                merge_sort(l, mid)
                merge_sort(mid+1, r)
                merge(l, mid, r)
        merge_sort(0, len(arr)-1)
        return res


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        arr=[] # array with indexes
        res=[0]*len(nums)
        
        # add (num, index) tuples
        for i,num in enumerate(nums):
            arr.append((num, i))
    
        def merge(left, right):
            l=0
            r=0
            out=[]
            numElemsRightArrayLessThanLeftArray=0
            while l < len(left) and r < len(right):
                if left[l][0] > right[r][0]:
                    out.append(right[r])
                    r += 1
                    numElemsRightArrayLessThanLeftArray += 1                 
                else:
                    out.append(left[l])
                    res[left[l][1]] += numElemsRightArrayLessThanLeftArray
                    l += 1
            if l < (len(left)):
                for i in range(l, len(left)):
                    out.append(left[i])
                    res[left[i][1]] += numElemsRightArrayLessThanLeftArray
            if r < (len(right)):
                for i in range(r,len(right)):
                    out.append(right[i])
            return out

        def merge_sort(arr):
            if len(arr)==1:
                return arr
            midIndex=len(arr)//2
            left_side=merge_sort(arr[:midIndex])
            right_side=merge_sort(arr[midIndex:])
            return merge(left_side, right_side)
        merge_sort(arr)
        return res