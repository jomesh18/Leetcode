'''
Maximum Units on a Truck
You are assigned to put some amount of boxes onto one truck. You are given a 2D array boxTypes, where boxTypes[i] = [number_of_boxesi, number_of_units_per_boxi]:

number_of_boxesi is the number of boxes of type i.
number_of_units_per_boxi is the number of units in each box of the type i.
You are also given an integer truckSize, which is the maximum number of boxes that can be put on the truck. You can choose any boxes to put on the truck as long as the number of boxes does not exceed truckSize.

Return the maximum total number of units that can be put on the truck.

 

Example 1:

Input: boxTypes = [[1,3],[2,2],[3,1]], truckSize = 4
Output: 8
Explanation: There are:
- 1 box of the first type that contains 3 units.
- 2 boxes of the second type that contain 2 units each.
- 3 boxes of the third type that contain 1 unit each.
You can take all the boxes of the first and second types, and one box of the third type.
The total number of units will be = (1 * 3) + (2 * 2) + (1 * 1) = 8.
Example 2:

Input: boxTypes = [[5,10],[2,5],[4,7],[3,9]], truckSize = 10
Output: 91
 

Constraints:

1 <= boxTypes.length <= 1000
1 <= number_of_boxesi, number_of_units_per_boxi <= 1000
1 <= truckSize <= 106
'''

class Solution:
    def maximumUnits(self, boxTypes: [[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda x:x[1], reverse=True)
        max_units = 0
        for number_of_boxes, number_of_units_per_box in boxTypes:
        	if truckSize < 0:
        		return max_units
        	if truckSize-number_of_boxes>=0:
        		max_units += number_of_boxes*number_of_units_per_box
        	else:
        		max_units += truckSize*number_of_units_per_box
        	truckSize -= number_of_boxes
        return max_units

boxTypes = [[1,3],[2,2],[3,1]]
truckSize = 4
# Output: 8

boxTypes = [[5,10],[2,5],[4,7],[3,9]]
truckSize = 10
# Output: 91

s = Solution()
print(s.maximumUnits(boxTypes, truckSize))
