'''
2326. Spiral Matrix IV
Medium

900

36

Add to List

Share
You are given two integers m and n, which represent the dimensions of a matrix.

You are also given the head of a linked list of integers.

Generate an m x n matrix that contains the integers in the linked list presented in spiral order (clockwise), starting from the top-left of the matrix. If there are remaining empty spaces, fill them with -1.

Return the generated matrix.

 

Example 1:


Input: m = 3, n = 5, head = [3,0,2,6,8,1,7,9,4,2,5,5,0]
Output: [[3,0,2,6,8],[5,0,-1,-1,1],[5,2,4,9,7]]
Explanation: The diagram above shows how the values are printed in the matrix.
Note that the remaining spaces in the matrix are filled with -1.
Example 2:


Input: m = 1, n = 4, head = [0,1,2]
Output: [[0,1,2,-1]]
Explanation: The diagram above shows how the values are printed from left to right in the matrix.
The last space in the matrix is set to -1.
 

Constraints:

1 <= m, n <= 105
1 <= m * n <= 105
The number of nodes in the list is in the range [1, m * n].
0 <= Node.val <= 1000
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        matrix = [[-1]*n for _ in range(m)]
        
        def find_next(r, c, direction, top_row, bottom_row, left_col, right_col):
            if direction == 0:
                if c+1 <= right_col:
                    c += 1
                else:
                    direction = 1
                    top_row += 1
                    r += 1
            elif direction == 1:
                if r+1 <= bottom_row:
                    r += 1
                else:
                    direction = 2
                    right_col -= 1
                    c -= 1
            elif direction == 2:
                if c - 1 >= left_col:
                    c -= 1
                else:
                    direction = 3
                    bottom_row -= 1
                    r -= 1
            elif direction == 3:
                if r-1 >= top_row:
                    r -= 1
                else:
                    direction = 0
                    left_col += 1
                    c += 1
            return (r, c, direction, top_row, bottom_row, left_col, right_col)
            
        matrix[0][0] = head.val
        curr_row, curr_col, direction = 0, 0, 0
        top_row, bottom_row, left_col, right_col = 0, m-1, 0, n-1
        curr = head.next
        while curr:
            curr_row, curr_col, direction, top_row, bottom_row, left_col, right_col = find_next(curr_row, curr_col, direction, top_row, bottom_row, left_col, right_col)
            # print(curr_row, curr_col, direction, top_row, bottom_row, left_col, right_col)
            matrix[curr_row][curr_col] = curr.val
            curr = curr.next
        return matrix