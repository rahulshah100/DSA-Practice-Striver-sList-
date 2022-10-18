# Problem: Set Matrix Zeros
# LeetCode Link: https://leetcode.com/problems/set-matrix-zeroes/submissions/

# Description: Given an m x n integer matrix, if an element is 0, set its entire row and column to 0's, and return the matrix. You must do it in place.

# Constraints: m == matrix.length
#              n == matrix[0].length
#              1 <= m, n <= 200
#              -2^31 <= matrix[i][j] <= 2^31 - 1

# Example:- Input: matrix = [[1,1,1],[1,0,1],[1,1,1]] Output: [[1,0,1],[0,0,0],[1,0,1]]
#           Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]] Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
# -------------------------------------------------------------------------------


# Approach 1: My Original Approach- Using an array of array to store the indexes of row,col where 0s are found. Using that array in an another iteration to mark 0s in matrix.
from typing import List  # So we can use descriptions such as List[List[int]]) -> None.

"""
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # Creating an Array Locating all the Zeroes
        LocateZeroes = []
        for rowIndex, rowItem in enumerate(matrix):
            for columnIndex, columnItem in enumerate(rowItem):
                if columnItem == 0:
                    LocateZeroes.append([rowIndex, columnIndex])

        # From LocateZeroes, making all the appropriate items as Zero
        totalRows = len(matrix)
        totalColumns = len(matrix[0])
        for RowColumnCordinate in LocateZeroes:
            currentRow = RowColumnCordinate[0]
            currentColumn = RowColumnCordinate[1]
            # Making all the columnItems Zero
            for pointer in range(0, totalColumns):
                matrix[currentRow][pointer] = 0
            # Making all the rowItems Zero
            for pointer in range(0, totalRows):
                matrix[pointer][currentColumn] = 0
    
        # Printing Final Answer
        print(matrix)


S = Solution()
# S.setZeroes([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
S.setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]])
"""
# Time Complexity: O((rows*columns)+(rows*column(columns + rows)) i.e.(O(m*n)+((m*n)*(m+n)). Explaination: Due to 2 for loops being there for Filling LocateZeroes we have O(m*n). It is added with O((m*n)*(m+n)) more time consumed during making items as Zero. Break down of O(m*n(m+n)): RowColumnCordinate would have total m*n items in worst case (see below explained space complexity) and for each item amongst those many two inner for loops would execute one after other for all the columns in that row where 0 is found i.e.m times and for all rows in that column where 0 is found i.e. n times; hence together it is (m*n)*(m+n). This Time Complexity could be generalized as O(m*n).
# Space Complexity: O(2(m*n)). Explaination: If all matrix items are 0, then m*n entries items would be stored in LocateZeroes. Each LocateZero Item has 2 items further. So, in worst case, total space consumed by that variable would be O(2(m*n)). This Space Complexity could be generalized as O(m*n).


# Approach 2: Better than Approach 1 in terms of space complexity.
# Modification: As even if one column in one row is found 0, the entire row is made 0; and vice versa if one column in one row is found 0 then all the columns in the matrix could be made 0. Hence in that terms, we dont need to keep track of a particular column in all the rows or a particular row in all the columns, if we have already encountered a 0 once there. This will save memory of storing coordinates. Also in approach 1 we can find we had to traverse through LocateZero and then in its every item we had to fetch the rows and columns of each located zero. Instead if we could split rows and column cordinates into seperate variables instead of storing in one LocateZeroes, we can directly have access to them and one iteration would be saved which will mean better time complexity, which is what is done here.
"""
class Solution(object):
    def setZeroes(self, matrix):        
        R = len(matrix)
        C = len(matrix[0])
        rows, cols = set(), set()

        # Essentially, we mark the rows and columns that are to be made zero
        for i in range(R):
            for j in range(C):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)

        # Iterate over the array once again and using the rows and cols sets, update the elements
        for i in range(R):  
            for j in range(C):
                if i in rows or j in cols:  #This will have O(m+n) time complexity given in rows we try finding the i first and it is not there and then in cols the we try finding j and it is the last item.
                    matrix[i][j] = 0  
"""
# Time Complexity: O((m*n)+((m*n)*(m+n))) where M and N are the number of rows and columns respectively. Explaintation:O(m*n) for traversing the matrix to fill rows and cols variable. Another O(m*n) time to traverse through all elem of the Matrix and in that using m+n complexity to verify for each elem if it's corresponding row, col value is there in the rows or cols matrix. In total that is O((m*n)+((m*n)*(m+n))).
# Space Complexity: O(M+N). Explaination: In worst case where all the items are zero then we'll have n row items in rows variable and m column items in cols variable. Together it'll make up m+n space used.


# Approach3: Better Space but compromised time complexity than the Approach 2.
# Constant Space Approach: Traverse the matrix from top left corner i.e. 0,0th row and column respectively to their indexes being 0,1... 0,2... 2,1..2,2, till the end and as a 0 value is found anywhere, check in that entire row i.e. for all the columns in that row and if theyre not 0 then change them to a string "Zero". Similary, check for all the rows for the same column and if a non-zero value is found then replace that with "Zero". We dont change the already found 0 as it might affect other items and could make them 0 so those initially found 0 items have to be preserved. After one such complete traversal, do an another traversal just to change "Zero" to 0.
# Time Complexity: O(((m*n)*(m+n))+(m*n)). Explaination: Total traversal iteration for identifying and placing "Zero" would be O(m*n). If all the items are 0 in the matrix, then for each iteration of O(m*n), we'll have to go to m rows and make the particular column entry 0; similary we'll have to go to n columns in the row where 0 is found, so to check the items and make them "Zero"; this in total were m+n more traversal for each 0 found in the matrix. Hence the worst time entity in the given approach is 0((m*n)*(m+n)). In addition, we'll do one one more traversal in matrix to change "Zero" to 0, which will take 0(m*n).As O((m*n)*(m+n)) supercedes the time taken by 0(m*n) and given these are very large values, we can generalize our above given answer by only writing O((m*n)*(m+n)).
# Space Complexity: O(1). Explaination: No extra space is used as changes are implemented in the given matrix itself.


# Approach4: Best Approach- Combining Time Complexity of Approach2 and Space Complexity of Approach3
# Modification: In approach 2 if we could avoid the space of those two extra variables i.e. rows and cols, by using first row and first column of the given matrix to store values stored by rows and cols variable, then that would result in approach4. Just as approach 2 we'll do 2 iterations here. In first iteration, we'll do mark down of 0's, and 2nd iteration to check and make the row, col items as 0 if in their corrsponding row/col there has been a zero. But in this case for 2nd iteration i.e. when updating elements to 0s, if any 0's are encountered in first row and if make all of the column items of first row as zero then further during second iteration we might see unwanted influence of those zeroes as they were used for marking purposes. For this we'll do two things. One, we'll iterate in reverse. Two, If any 0 is found in first row, we'll not change any column item of the first row but will change a variable's value to true; this will just be used as an indication that first row has to be made 0. Similarly for first column we'll use a such variable with its initial value false; if any row is having 0 in its first column then this variable would be changed to true.
class Solution():
    def setZeroes(self, matrix):
        # print(matrix)
        changeFirstRowToZero = False
        changeFirstColToZero = False

        if type(matrix[0]) == int:  # For cases where matrix is 1D like matrix=[1,0]
            changeAllItemsToZero = False
            for items in matrix:
                if items == 0:
                    changeAllItemsToZero = True
            if changeAllItemsToZero:
                for index in range(len(matrix)):
                    matrix[index]=0
            print(matrix)
            return
        else:
            totalRows = len(matrix)
            totalCols = len(matrix[0])

        # Marking down 0s.
        for RowIndex, RowItem in enumerate(matrix):
            for ColIndex, ColItem in enumerate(RowItem):
                if matrix[RowIndex][ColIndex] == 0:
                    if RowIndex == 0:
                        changeFirstRowToZero = True
                    elif ColIndex == 0:
                        changeFirstColToZero = True
                    else:
                        matrix[0][ColIndex] = 0
                        matrix[RowIndex][0] = 0

        # Visiting each item from reverse, and checking if their corresponding 1strow, 1stcol values show 0s, if so then mark item as 0.
        for RowIndex in range(totalRows - 1, -1, -1):
            for ColIndex in range(totalCols - 1, -1, -1):
                if matrix[0][ColIndex] == 0 or matrix[RowIndex][0] == 0:
                    matrix[RowIndex][ColIndex] = 0

        # Making 1st row, 1st col as zero if any item in them were zero in the original matrix.
        if changeFirstRowToZero == True:
            for items in range(totalCols):
                matrix[0][items] = 0
        if changeFirstColToZero == True:
            for items in range(totalRows):
                matrix[items][0] = 0

        print(matrix)


S = Solution()
# S.setZeroes([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
# S.setZeroes([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]])
# S.setZeroes([[1, 2, 3, 4], [5, 0, 7, 8], [0, 10, 11, 12], [13, 14, 15, 0]])
# S.setZeroes([[1, 0, 3]])
# S.setZeroes([1, 0])

# Time Complexity: O(2(m*n))
# Space Complexity: O(1)
