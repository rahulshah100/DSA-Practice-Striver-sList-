# https://leetcode.com/problems/rotate-image/

# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees(clockwise).

# You have to rotate the image in -place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]] Output: [[7,4,1],[8,5,2],[9,6,3]]
# Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]] Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

# Constraints:
# n == matrix.length == matrix[i].length
# 1 <= n <= 20
# -1000 <= matrix[i][j] <= 1000
# ---------------------------------------------------------------------------------------------------------------------------------------------

# Approach 1: We'll convert all the rows to columns i.e. Transpose the matrix and then reverse all the items in each row of this transposed matrix.
# For [[1,2,3],[4,5,6],[7,8,9]] we'll convert it firstly into [[1,4,7],[2,5,8],[3,6,9]]
from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        NumberOfRowsColumns=len(matrix)
        # Transposing the matrix: matrix[1,0] will become matrix[0,1], matrix [1,2] will become matrix of [2,1] and so on...
        for i in range(NumberOfRowsColumns):
            for j in range(i+1, NumberOfRowsColumns):
                temp=matrix[j][i]
                matrix[j][i]=matrix[i][j]
                matrix[i][j]=temp
            print(matrix)
        # Reversing rows.
        lower=0
        higher=NumberOfRowsColumns-1
        for i in range(NumberOfRowsColumns):
            while lower<higher:
                temp=matrix[i][lower]
                matrix[i][lower]=matrix[i][higher]
                matrix[i][higher]=temp
                lower+=1
                higher-=1
            lower=0
            higher=NumberOfRowsColumns-1
        print(matrix)

S=Solution()
S.rotate([[1,2,3],[4,5,6],[7,8,9]])
S.rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]])
# Time Complexity: O(n^2), given that the matrix is shown as n. Explanation: for calculating the transponse of matrix, we are using two for loops in which for first iteration the inner for loop will run for n-1 times, then for second iteration of outer for loop, the inner for loop will run for n-2 times and so on upto 0 times at last. This is Binomial Sum of iterations, and total iterations here are O(N(N+1)/2). For reversing the rows the outer for loop will run for n times. Each time making inner for loop run for (n-1)/2 or n/2 times depending on whether the n is odd or even respectively. As (n-1)/2= n/2-1/2, by removing constant we get n/2 and hence for inner while loop, regardless of n being odd or even, we can consider it's time complexity as n/2. Therefore in case of reversing the rows total time complexity=n(n/2). Total=n(n/2)+(n(n+1)/2). This is generalized as O(n^2).
# Space Complexity: O(1)
