# https://leetcode.com/problems/search-a-2d-matrix/

# Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:
# Integers in each row are sorted from left to right. The first integer of each row is greater than the last integer of the previous row.

# Example1:Input: matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target = 3 Output: true
# Example2: Input: matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target = 13 Output: false

# Constraints:
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 100
# -10^4 <= matrix[i][j], target <= 10^4
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Approach1:go through all array items and further all sub-items to compare if item matches.
from typing import List

"""class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j]==target:
                    print(True)
                    return True
        print(False)
        return False
S=Solution()
S.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3)"""
# TimeComplexity:O(mn)
# SpaceComplexity:O(1)


# Approach2: We start from the last item of first row, if the given number is bigger, we move down from there i.e.go to 2nd row last item, if item is smaller than this then now go to left i.e.2nd row 2nd last item, still if item is smaller we move further to left i.e.2nd row 3rd last item. If here, item is found bigger we move down (more efficient with constraints given in the question:"The first integer of each row is greater than the last integer of the previous row." would be to here return False at this point) i.e.3rd row 3rd last item. We'll do this till either we move out of the columns going left left left or move out of the rows going down down down.
"""class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = 0
        col = len(matrix[0]) - 1
        while (row <= (len(matrix) - 1) and col >= 0):  # Important Observation: in python 'and' is normal 'and', and '&' is bitwise 'and'.
            if matrix[row][col] == target:
                # print(row, col, row <= (len(matrix) - 1), col >= 0)
                return True
            elif matrix[row][col] < target:
                # print(row, col, row <= (len(matrix) - 1), col >= 0)
                row += 1
            elif matrix[row][col] > target:
                # print(row, col, row <= (len(matrix) - 1), col >= 0)
                col -= 1
        # print("Outside", row, col, row<=(len(matrix)-1), col>=0)
        return False


S = Solution()
# print(S.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 17))
print(S.searchMatrix([[1]], 0))"""
# Time Complexity: O(n+m). Maximum, we'll travel all the way down from top right corner and then all the way left from there till we are out of the matrix. Given rows are m and there are n items in each rows, while going down we'll take m steps max and to the left max n steps. So total max steps=m+n.
# Space Complexity: O(1)


# Approach 3: As we can see the subitems of all arrays, even holistically they're all sorted. In such case if we can flatten the 2D array into 1D then we can use BinarySearch on it. But to flatten the array, we will have to use for loops to either traverse through all list items and store them in seperate array which increases space complexity or we can store in the same/given array, for m times, taking first item and traversing through it completely and appending all items inthe same array and then deleting the item; but even this will increase time complexity by O(m*n). Therefore, what we'll do is in Binary search instead of flattening, we'll use the 2D array by figuring how to pass the appropriate indexes for the given 2D array.
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low = 0
        high = (len(matrix) * len(matrix[0])) - 1
        while high >= low:
            mid = (low + high) // 2
            print('low-', low, 'high-', high, 'mid-', mid, 'row-', (mid // len(matrix[0])), 'col-',( mid % len(matrix[0])), 'matrixVal-', matrix[mid // len(matrix[0])][mid % len(matrix[0])])
            if matrix[mid // len(matrix[0])][mid % len(matrix[0])] == target:  # this is the part we had to figure out here, that how to represent rows and columns.
                return True
            elif matrix[mid // len(matrix[0])][mid % len(matrix[0])] > target:
                high = mid - 1
            else:
                low = mid + 1
        return False


S = Solution()
print(S.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 60))
# Time Complexity: O(log(mn))
# Space Complexity: o(1)