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
# Approach1: Using an extra `visited` array that has m rows with n cols, wherein each items is 1 and a `moves` string along with current row and current col as params we chart out a recursive function. Initially with row, col as 0, 0 this function is called where it checks first for base condition wherein if row, col = n-1, n-1 meaning we are at destination/bottom-right block and that's where we append moves into an answer array. If it's not base condition, we will expand flow of our execution in 4 directions: D, L, R, U as is Lexographical order, to use which we have been asked in Quesition as a Note. First we'll check for D if the new coordinates don't violate condition of visiting an already visited index, coordinates being out of the grid and there being a 0 in the givenGrid at newCordinates in either of which cases we'll return False, or else True. For a True, the new Direction is safe to take and so first we block the new cordinate in visited array with a 0 and put a recursive call with updated coordinates, updated visitedArray and moves appended with a D. Below recursion we mend back the visitedArray by updating it's checked coordinates with a 0 showing they're unvisited. Same for other 3 directions. At the end we return ans Array.
class Solution:
    def findPath(self, m, n):
        visited = [[1 for i in range(n)] for i in range(n)]
        ans = []

        if m[0][0] == 0: #This has to be put because below for down which is first condition, we are only checking for incremented column itself where this case will lapse
            return ans

        def helperFunc(row, col, visited, moves):
            if row == n - 1 and col == n - 1:
                ans.append(moves)

            # down
            if check(row + 1, col, m, visited, n):
                visited[row][col] = 0
                helperFunc(row + 1, col, visited, moves + 'D')
                visited[row][col] = 1
            # left
            if check(row, col - 1, m, visited, n):
                visited[row][col] = 0
                helperFunc(row, col - 1, visited, moves + 'L')
                visited[row][col] = 1
            # right
            if check(row, col + 1, m, visited, n):
                visited[row][col] = 0
                helperFunc(row, col + 1, visited, moves + 'R')
                visited[row][col] = 1
            # up
            if check(row - 1, col, m, visited, n):
                visited[row][col] = 0
                helperFunc(row - 1, col, visited, moves + 'U')
                visited[row][col] = 1

        helperFunc(0, 0, visited, "")
        return ans


def check(currRow, currCol, givenMatrix, visitedMatrix, n):
    if 0 <= currRow < n and 0 <= currCol < n and givenMatrix[currRow][currCol] == 1 and visitedMatrix[currRow][currCol] == 1:
        return True
    return False


S = Solution()
print(S.findPath([[1, 0, 0, 0],
                  [1, 1, 0, 1],
                  [1, 1, 0, 0],
                  [0, 1, 1, 1]], 4))

# TC: O(4^(mn)) Explanation: For each call we have 4 more calls to unveil. In each of these 4 calls there are further 4 more calls and so on. There being mn total items, here total calls are like 4(4(4(4.... total of mn times which gives us 4^mn.
# SC: O(3mn) Explanation: for max depth of recursion it could be traversing all the elements i.e.mn. Plus visited array takes up mn more space. Given recusion's depth, move could be storing 1 direction from each call storing a total of mn directions.



# Approach2: Readability Improvements to Approach1- just reducing 4 if-statements by one for loop. We can use 2 arrays each holding difference that needs to be accounted in row and col respectively to undergo next step as either of DLRU. We'll also use a string to store "DLRU" so to be able to fetch the direction that can be appended into moves, once we're iteraing through for-loop. With 2 arrays what was meant is for taking down how row,col becomes=>row+1,col so 2 arrays will store [1] [0]. Similaryl, collectively for all directions, our 2 arrays are- [1, 0, 0, -1] [0,-1,1,0]. This will not at all create difference in TC. With SC too, constant extra space for di, dj and lexOrder is only added which are ignored as they're constant.
class Solution:
    def findPath(self, m, n):
        visited = [[1 for i in range(n)] for i in range(n)]
        ans = []
        di=[1, 0, 0, -1]
        dj=[0,-1,1,0]
        lexOrder="DLRU"

        if m[0][0] == 0:
            return ans

        def helperFunc(row, col, visited, moves):
            if row == n - 1 and col == n - 1:
                ans.append(moves)

            for i in range(4):
                if check(row + di[i], col + dj[i], m, visited, n):
                    visited[row][col] = 0
                    helperFunc(row + di[i], col + dj[i], visited, moves + lexOrder[i])
                    visited[row][col] = 1

        helperFunc(0, 0, visited, "")
        return ans


def check(currRow, currCol, givenMatrix, visitedMatrix, n):
    if 0 <= currRow < n and 0 <= currCol < n and givenMatrix[currRow][currCol] == 1 and visitedMatrix[currRow][currCol] == 1:
        return True
    return False


S = Solution()
print(S.findPath([[1 ,1],[1,1]], 2))
# TC: Same as Approach1
# SC: Same as Approach1