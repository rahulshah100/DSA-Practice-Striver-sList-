 # Problem: Set Matrix Zeros
# LeetCode Link: https://leetcode.com/problems/set-matrix-zeroes/submissions/

# Description: Given an m x n integer matrix, if an element is 0, set its entire row and column to 0's, and return the matrix. You must do it in place.

# Constraints: m == matrix.length
#              n == matrix[0].length
#              1 <= m, n <= 200
#              -2^31 <= matrix[i][j] <= 2^31 - 1

# Example:- Input: matrix = [[1,1,1],[1,0,1],[1,1,1]] Output: [[1,0,1],[0,0,0],[1,0,1]]
#           Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]] Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
# ----------------------------------------------------------------------------------------------
# Python Basics
#         a = {1, 1, 2} #Set is unordered collections of unique elements. It is unordered because it's been randomized in the way hashing is easier. Hence it's elem look up time is O(1) like dictionary's and unlike array's. But because set is randomized even though it is mutable, you cant per say reassign the elems. We can add, lookup and remove the items tho. If we print this set we'll see it to have 1 only once. Also coz of randomized order set[i] gives error, but `for i in set: print i` does get job done
#         b = {1: 2, 2: 's'} #Dictionary - accessible values by keys
#         c = (1, 21, 1, 1) #Tuples - Immutable
#         d = [12, 'as'] #List/Arrays
#         e = set() #Another way to define a set, if it's empty
#         print(type(a), a, type(b), b, type(c), c, type(d), d, type(e), e)
#
#         '&' is a bitwise AND-Operator in python wherease 'and' is a conditional AND
# ------------------------------------------------------------------------------------------------
# Approach 1: My Original Approach- Using an array of arrays to store the indexes of row,col where 0s are found. Using that array in an another iteration to mark 0s in matrix.
#Note we wont have to take care of end case where matrix is a 1D, given the constraints
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
# Time Complexity: O((rows*columns)+(rows*column(columns + rows)) i.e.O(mn+ mn(m+n)). Explaination: Due to 2 for loops being there for Filling LocateZeroes we have O(m*n). It is added with O(mn(m+n)) more time consumed during making items as Zero. Break down of O(mn(m+n)): RowColumnCordinate would have total mn items in worst case (see below explained space complexity) and for each item amongst those many two inner for loops would execute one after other for all the columns in that row where 0 is found i.e. m times and for all rows in that column where 0 is found i.e. n times; hence together it is (m*n)*(m+n). This Time Complexity could be generalized as O(m*n).
# Space Complexity: O(2(m*n)). Explaination: If all matrix items are 0, then m*n entries items would be stored in LocateZeroes. Each LocateZero Item has 2 items further. So, in worst case, total space consumed by that variable would be O(2(m*n)). This Space Complexity could be generalized as O(m*n).


# Approach 2: Better than Approach 1 in terms of space complexity.
# Modification: Using just 2 Sets, one for each: rows and the column, instead of Array of Arrays. As even if one column in one row is found 0, the entire row is made 0; and vice versa if one column in one row is found 0 then all the columns in the matrix could be made 0. Hence in that terms, we dont need to keep track of a particular column in all the rows or a particular row in all the columns, if we have already encountered a 0 once there. This will save memory of storing coordinates. Also in approach 1 we can find we had to traverse through LocateZero and then in its every item we had to fetch the rows and columns of each located zero. Instead if we could split rows and column cordinates into seperate variables instead of storing in one LocateZeroes, we can directly have access to them and one iteration would be saved which will mean better time complexity, which is what is done here.
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
# Time Complexity: O(mn + mn(m+n)) where M and N are the number of rows and columns respectively. Explaintation:O(m*n) for traversing the matrix to fill rows and cols variable. Another O(m*n) time to traverse through all elem of the Matrix and in that using m+n complexity to verify for each elem if it's corresponding row, col value is there in the rows or cols matrix. In total that is O((m*n)+((m*n)*(m+n))).
# Space Complexity: O(M+N). Explaination: In worst case where all the items are zero then we'll have n row items in rows variable and m column items in cols variable. Together it'll take up m+n space used.


# Approach3: Improved SC than Approach2
# In Approach 2 instead of later iterating through whole matrix checking for each index if that row is in the set of markedRows or if so it the col Coord, we'll do seperate iterations directly over set of markedRows and then markedCols, each in which we traverse cols and rows for respective markedRows, markedCol set Coord.
"""class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])
        rowCoords, colCoords = set(), set()
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j]==0:
                    rowCoords.add(i)
                    colCoords.add(j)
        for i in rowCoords:
            for j in range(cols):
                matrix[i][j]=0
        for i in colCoords:
            for j in range(rows):
                matrix[j][i]=0
        return matrix
"""
# TC: O(mn + mn + mn) Explanation: Generalized as mn time we have 3 mn Time Complexities that are summed up, resulting due to traversing first to build set for row, col, then another for say traversing all n cols for m rows that are part of rows Set creating a mn TC requirement and similarly mn more TC for traversing colCoords
# SC: O(m+n)


# Approach4: Better Space complexity than the Approach 3.
# Constant Space Approach: Traverse the matrix and as a 0 value is found anywhere, check in that entire row i.e. for all the columns in that row and if theyre not 0 then change them to a string "Zero". Similary, check for all the rows for the same column and if a non-zero value is found then replace that with "Zero". We dont change the already found 0 as it might affect other items and could make them 0 so those initially found 0 items have to be preserved. After one such complete traversal, do an another traversal just to change "Zero" to 0.
"""
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    print([i,j])
                    for x in range(len(matrix)):
                        if matrix[x][j]!=0:
                            matrix[x][j]='0'
                    for y in range(len(matrix[0])):
                        if matrix[i][y] != 0:
                            matrix[i][y]='0'
        print(matrix)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]=='0':
                    matrix[i][j]=0
        print(matrix)
"""
# Time Complexity: O(mn(m+n)+ mn). Explaination: Total traversal iteration for identifying and placing "Zero" would be O(m*n). If all the items are 0 in the matrix, then for each iteration of O(m*n), we'll have to go to m rows and make the particular column entry 0; similary we'll have to go to n columns in the row where 0 is found, so to check the items and make them "Zero"; this in total were m+n more traversal for each 0 found in the matrix. Hence the worst time entity in the given approach is 0((m*n)*(m+n)). In addition, we'll do one one more traversal in matrix to change "Zero" to 0, which will take 0(m*n).As O((m*n)*(m+n)) supercedes the time taken by 0(m*n) and given these are very large values, we can generalize our above given answer by only writing O((m*n)*(m+n)).
# Space Complexity: O(1). Explaination: No extra space is used as changes are implemented in the given matrix itself.


# Approach5: Best Approach - Use First Row and Col to indicate whether that whole row and col respectively have to be made 0.
# Modification: Two iterations. In first iteration we go through all matrix elems if they are 0 we check if they're in firstCol or firstRow in case of which we maintain two seperate variables indicating if first row or first col has to be made 0. If any other elems are found, the corresponding col and rows first elems are made 0. In second iteration we iterate through all matrix elems again, this time skipping all first row and first col items. We check whether the corresponding row or col has 0, which if so we make this elem as 0. Last if variables indicating row or column is 0 is true we change all elems in the first row or first col respectively to 0.
class Solution():
    def setZeroes(self, matrix):
        TotCols = len(matrix[0])
        TotRows = len(matrix)
        FirstRowZero = False
        FirstColZero = False
        for i in range(TotRows):
            for j in range(TotCols):
                if matrix[i][j] == 0:
                    if i == 0:
                        FirstRowZero = True
                    if j == 0:
                        FirstColZero = True
                    else:
                        matrix[0][j] = 0
                        matrix[i][0] = 0

        for i in range(1, TotRows):
            for j in range(1, TotCols):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0

        if FirstRowZero:
            for i in range(TotCols):
                matrix[0][i] = 0
        if FirstColZero:
            for i in range(TotRows):
                matrix[i][0] = 0

        print(matrix)

S = Solution()
# S.setZeroes([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
# S.setZeroes([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]])
# S.setZeroes([[1, 2, 3, 4], [5, 0, 7, 8], [0, 10, 11, 12], [13, 14, 15, 0]])
# S.setZeroes([[1, 0, 3]])
# S.setZeroes([1, 0])

# Time Complexity: O(2mn + m + n) Explanation: Two matrix iteration and in case FirstRowZero is True we'll take n time making all those columns Zero, if FirstColZero is True we'll take m time similarly.
# Space Complexity: O(1)
