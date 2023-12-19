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
# Approach1: Create a transitionary/dummy matrix same as the given one. Arrange elements in wanted fashion in that one from the given one, and later make given one equal to dummy matrix
from typing import List
import copy

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        dumMatrix=copy.deepcopy(matrix) #NOTE the way I have copied. It's the copy by reference problem in python. So for all derived data structures this needs to be done for copying.
        # dumMatrix=matrix[:] #NOTE this didn't work coz this is shallow copy where although new array is created, the inner items are referenced from same mem. location where the array from which it has copied has been
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                dumMatrix[j][len(matrix)-1-i]=matrix[i][j] #This is where instead if we did matrix[j][len(matrix)-1-i]=dumMatrix[i][j] our solution ends!
        # matrix=copy.deepcopy(dumMatrix) #NOTE this didn't work, as in this problem we were asked to change in-place and not reassign or return anything. Hence, leet-code has a certain way to track the variable and it either looses that track if the variable is reassigned or doesn't count that valid due to in-place specification.
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                matrix[i][j] = dumMatrix[i][j]

# TC: O(3(n^2))
# SC: O(n^2)



# Approach 2: We'll convert all the rows to columns i.e. Transpose the matrix and then reverse all the items in each row of this transposed matrix.
# For [[1,2,3],[4,5,6],[7,8,9]] we'll convert it firstly into [[1,4,7],[2,5,8],[3,6,9]]
from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # Transposing the matrix: matrix[1,0] will become matrix[0,1], matrix [1,2] will become matrix of [2,1] and so on...
        for i in range(len(matrix)):
            for j in range(i, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # Reversing Matrix
        for i in range(len(matrix)):
            l = 0
            u = len(matrix) - 1
            while l < u:
                matrix[i][l], matrix[i][u] = matrix[i][u], matrix[i][l]
                l += 1
                u -= 1
        print(matrix)

S=Solution()
S.rotate([[1,2,3],[4,5,6],[7,8,9]])
S.rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]])
# Time Complexity: O(n^2), given that the matrix is shown as n. Explanation: for calculating the transpose of matrix, we are using two for loops in which for first iteration the inner for loop will run for n-1 times, then for second iteration of outer for loop, the inner for loop will run for n-2 times and so on upto 0 times at last. This is Binomial Sum of iterations, and total iterations here are O(N(N+1)/2). For reversing the rows the outer for loop will run for n times. Each time making inner for loop run for (n-1)/2 or n/2 times depending on whether the n is odd or even respectively. As (n-1)/2= n/2-1/2, by removing constant we get n/2 and hence for inner while loop, regardless of n being odd or even, we can consider its time complexity as n/2. Therefor in case of reversing the rows total time complexity=n(n/2). Total=n(n/2)+(n(n+1)/2). This is generalized as O(n^2).
# Space Complexity: O(1)
