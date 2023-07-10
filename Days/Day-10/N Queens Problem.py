# https://leetcode.com/problems/n-queens/

# The n - queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other. Given an integer n, return all distinct solutions to the n - queens puzzle.You may return the answer in any order. Each solution contains a distinct board configuration of the n - queens ' placement, where ' Q ' and '. ' both indicate a queen and an empty space, respectively.

# Example1:
# Input: n = 4
# Output: [[".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]]
# Explanation: There exist two distinct solutions to the 4 - queens puzzle as shown above

# Example2:
# Input: n = 1
# Output: [["Q"]]

# Constraints:
# 1 <= n <= 9
# ------------------------------------------------------------------------------------------------------------------------------
# Approach1: Backtracking- Create an array givenArr of n arrays each of which has n '.' items, to make up for a mock empty n*n Grid. We will iterate through the first row of the giveArr, checking in each iteration if pertinent to current row putting a 'Q' only at the spot pointed by currentIteration is feasible. If so, we'll put the 'Q' there in the givenArr and now shift to figuring 'Q' arrangement for second row, by recursively calling the function this time with an incremented row. Recursive function we'll be passed params of givenArr and currRow. If putting 'Q' at spot pointed by currentIndex is not feasible we'll simply let iteration of loop increment. To ensure that for each iteration we're checking for a 'Q' only at that spot and no other columns have it, we'll use backtracking technique wherein once returned from recursive call we'll modify the spot in givenArr where we placed a 'Q' before recursion with now a '.'. Within the recursive function for a base condition we'll check if row has become n i.e. starting from 0th row we've managed finding a feasible spot to put 'Q' and called recursion with incremented row, and while doing so we've managed coming all the way where now row==n which means even for n-1th row that is last row we've found the feasible way to put 'Q'; this is where we have a solution and we'll append givenArr in a solutionArr after making each subArr of givenArr into a string. At end we'll return solution. For checking if putting 'Q' at given row, col is feasible as we know in a row we're placing only one 'Q' and that we are going row by row, we know beneath current row we don't need to check for any clash and so dont we for the same row. Hence we'll check only for all the rows above it in the same col, and in two upper diagonals- one going to right and other going left for there to not be any "Q".
from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        givenArr = [['.' for i in range(n)] for i in range(n)]
        solution = []

        def helperFunc(row):
            if row == n: solution.append([''.join(i) for i in givenArr])

            for i in range(n):
                if (QueenAt(row, i, n, givenArr)):
                    givenArr[row][i] = "Q"
                    helperFunc(row + 1)
                    givenArr[row][i] = "."

        helperFunc(0)
        return solution


def QueenAt(currRow, currCol, totalCol, currGrid):
    # checking only upwards, in same column
    row = currRow - 1
    while row >= 0:
        if currGrid[row][currCol] == "Q": return False
        row -= 1

    # checking for up-right diagonal
    row, col = currRow - 1, currCol + 1
    while row >= 0 and col < totalCol:
        if currGrid[row][col] == "Q": return False
        row, col = row - 1, col + 1

    # checking for up-left diagonal
    row, col = currRow - 1, currCol - 1
    while row >= 0 and col >= 0:
        if currGrid[row][col] == "Q": return False
        row, col = row - 1, col - 1

    return True


S = Solution()
print(S.solveNQueens(4))
# TC: O(n^2 + ((n^2)!)(3n + n^2)) Explanation: n^2 to run a nested for loop to fill givenArr. Further, as we learnt earlier the total permutations amongst an array size n are always n!. So here there being n^2 items, (n^2)! is time all the function calls will take. Within each call we also run QueenAt which runs 3 while loop, contributing to more 3n TC. Also for base condition we have to add TC. Considering worst case we'll say all calls made it to base case and that's where n times to join n items, there is an additional TC of n^2.
# SC: O(n + n^2) Explanation: n is length of longest recursive call chain i.e.stack space, plus givenArr will be holding n^2 items throughout, so that's an addition SC. We ignore solution array's space as that's imperative to be returned for what's asked