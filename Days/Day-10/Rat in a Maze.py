# https://practice.geeksforgeeks.org/problems/rat-in-a-maze-problem/1

# Consider a rat placed at (0, 0) in a square matrix of order N * N. It has to reach the destination at (N - 1, N - 1). Find all possible paths that the rat can take to reach from source to destination. The directions in which the rat can move are 'U'(up), 'D'(down), 'L' (left), 'R' (right). Value 0 at a cell in the matrix represents that it is blocked and rat cannot move to it while value 1 at a cell in the matrix represents that rat can be travel through it.
# Note: In a path, no cell can be visited more than one time. If the source cell is 0, the rat cannot move to any other cell.

# Example 1:
# Input:
# N = 4
# m[][] = {{1, 0, 0, 0},
#          {1, 1, 0, 1},
#          {1, 1, 0, 0},
#          {0, 1, 1, 1}}
# Output:
# DDRDRR DRDDRR
# Explanation:
# The rat can reach the destination at
# (3, 3) from (0, 0) by two paths - DRDDRR
# and DDRDRR, when printed in sorted order
# we get DDRDRR DRDDRR.

# Example 2:
# Input:
# N = 2
# m[][] = {{1, 0},
#          {1, 0}}
# Output:
# -1
# Explanation:
# No path exists and destination cell is
# blocked.

# Your Task:
# You don't need to read input or print anything. Complete the function printPath() which takes N and 2D array m[ ][ ] as input parameters and returns the list of paths in lexicographically increasing order.
# Note: In case of no path, return an empty list. The driver will output "-1" automatically.

# Expected Time Complexity: O((3N^2)).
# Expected Auxiliary Space: O(L * X), L = length of the path, X = number of paths.

# Constraints:
# 2 ≤ N ≤ 5
# 0 ≤ m[i][j] ≤ 1
# ------------------------------------------------------------------------------------------------------------------------------------
# Approach1: To keep track of not repeating directions we'll use a visitedArr which would be of same dimension as to given maze/m but filled with 0s initially. Now a catch to this question is Lexicographic order of direction only gives us correct answer that is if we check for D,L,R,U; while L,R,D,U gives incorrect answer. So starting with row, col as 0,0 in a helperfunc we'll check if currRow and currCol is not 0 in given maze, otherwise we'll just return. Conversely, if maze for the current indices is 1 we'll recursively call this function for 'D' direction i.e. row-1 and col; and to reflect this change we'll keep and append a temp array which will now have a 'D', alongside making this row,col entry as 1 in visitedArr. While backtracking if this call returns we'll pop temp and append 'L' and recursively call a function for row, col-1. Similarly, we'll do for 'R' and 'U' directions. After which if we still had to go backtrack we'll undo visitedArr for this index by making it 0. Base condition is where row==col==len(maze)-1 and maze[row][col]==1. Alongside returning when currRow and currCol is 0, we'll also add onto it the conditions where visited is 1 or row<0 or row>=len(maze) or col<0 or col>=len(maze).
class Solution:
    def findPath(self, m, n):
        return self.helperfunc([], [[0 for i in range(n)] for j in range(n)], m, 0, 0, [])

    def helperfunc(self, temp, visitedArr, maze, row, col, ansArr):
        if row == col == len(maze) - 1 and maze[row][col] == 1:
            ansArr.append(''.join(temp))
            return ansArr
        elif row < 0 or col < 0 or row >= len(maze) or col >= len(maze[0]) or visitedArr[row][col] == 1 or maze[row][col] == 0:
            return [] #And not return so that in case where (m,n) are ([0,1,1],1) we wont get None returned

        visitedArr[row][col] = 1
        temp.append('D')
        self.helperfunc(temp, visitedArr, maze, row + 1, col, ansArr)
        temp.pop()

        temp.append('L')
        self.helperfunc(temp, visitedArr, maze, row, col - 1, ansArr)
        temp.pop()

        temp.append('R')
        self.helperfunc(temp, visitedArr, maze, row, col + 1, ansArr)
        temp.pop()

        temp.append('U')
        self.helperfunc(temp, visitedArr, maze, row - 1, col, ansArr)
        temp.pop()

        visitedArr[row][col] = 0
        return ansArr

S = Solution()
print(S.findPath([[1, 0, 0, 0], [1, 1, 0, 1], [1, 1, 0, 0], [0, 1, 1, 1]], 4))
print(S.findPath([[1, 0], [1, 0]], 2))
print(S.findPath([[0, 1, 0], [0, 0, 0],[1,1,1]], 3))
# TC: O(4^(mn)) Explanation: For each call we have 4 more calls to unveil. In each of these 4 calls there are further 4 more calls and so on. There being mn total items, here total calls are like 4(4(4(4.... total of mn times which gives us 4^mn.
# SC: O(3mn) Explanation: for max depth of recursion it could be traversing all the elements i.e. mn. Plus visitedArr takes up mn more space. Given recusion's depth, temp could be storing 1 direction from each call storing a total of mn directions in worst case.