# https://leetcode.com/problems/sudoku-solver/

# Write a program to solve a Sudoku puzzle by filling the empty cells. A sudoku solution must satisfy all of the following rules:
# Each of the digits 1 - 9 must occur exactly once in each row.
# Each of the digits 1 - 9 must occur exactly once in each column.
# Each of the digits 1 - 9 must occur exactly once in each of the 9 3 x3 sub - boxes of the grid.
# The '.' character indicates empty cells.

# Example1:
# Input: board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
#                 ["6", ".", ".", "1", "9", "5", ".", ".", "."],
#                 [".", "9", "8", ".", ".", ".", ".", "6", "."],
#                 ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
#                 ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
#                 ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
#                 [".", "6", ".", ".", ".", ".", "2", "8", "."],
#                 [".", ".", ".", "4", "1", "9", ".", ".", "5"],
#                 [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
# Output: [["5", "3", "4", "6", "7", "8", "9", "1", "2"],
#          ["6", "7", "2", "1", "9", "5", "3", "4", "8"],
#          ["1", "9", "8", "3", "4", "2", "5", "6", "7"],
#          ["8", "5", "9", "7", "6", "1", "4", "2", "3"],
#          ["4", "2", "6", "8", "5", "3", "7", "9", "1"],
#          ["7", "1", "3", "9", "2", "4", "8", "5", "6"],
#          ["9", "6", "1", "5", "3", "7", "2", "8", "4"],
#          ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
#          ["3", "4", "5", "2", "8", "6", "1", "7", "9"]]

# Constraints:
# board.length == 9
# board[i].length == 9
# board[i][j] is a digit or '.'.
# It is guaranteed that the input board has only one solution.
# -----------------------------------------------------------------------------------------------------------------------------------
# Approach1: We'll traverse through the given board in left to right fashion starting first row, then second row and so on... where using a helperfunc, in one function call we'll check for a singular coordinate i.e. a row, col index and try finding it a valid value. For finding valid value, over this coordinate we'll check for all values from 1 to 9 if they 1) aren't repeated in that row, or col 2)in that 3x3 block where current coordinate belong. If this is true it means we found a value for this coordinate, and we make a new function call for next col in same row. Also at the start of helpfunc we'll check if current coord doesn't hold a number already, because if so it's given as a part of question then we don't wanna change that and therefor we don't do anything but return a new func call with incremented col in same row. Now chances also are when we find a suiting value for row,col=0,7 and it further found suiting value for 0,8 and then 1,0 but for 1,1 we cant find any suiting value with this arrangement hence as we backtrack we check if we are coming from when row has been made 9 i.e. all the way through or from somewhere in between if it's somewhere in between then before backtracking we wanna make the changed value back to '.' at their corresponding coordinate. And hence at end of func we return False while for row==9 we return True. Thus conditions in helperfunc are to check at the start whether row==9 or col==9 in which cases we'll return True, or a new func call with incremented row and col made as 0, respectively.
from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        return self.helperfunc(0, 0, board)

    def helperfunc(self, row, col, board):
        if row == 9:
            return True  # The puzzle is solved

        if col == 9:
            return self.helperfunc(row + 1, 0, board)

        if board[row][col] == ".":
            for j in range(1, 10):
                if self.validate(str(j), row, col, board):
                    board[row][col] = str(j)
                    if self.helperfunc(row, col + 1, board):
                        return board  # Puzzle is solved
                    board[row][col] = "."  # Backtrack if the current choice doesn't lead to a solution
        else:
            return self.helperfunc(row, col + 1, board)

        return False  # No valid choice found for the current cell

    def validate(self, value, row, col, board):
        # check for rows, cols
        for i in range(9):
            if board[row][i] == value or board[i][col] == value:
                return False

        # check for the same block
        blockStart_Row = (row // 3) * 3
        blockStart_Col = (col // 3) * 3
        for i in range(3):
            for j in range(3):
                if board[blockStart_Row + i][blockStart_Col + j] == value:
                    return False

        return True

S = Solution()
board = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
print(S.solveSudoku(board))
# TC: O(9^(nm)) Explanation: For first coord we've 9 options, and something got selected say 7. With this now for 2nd coord on basis of this arrangement we found 8 but then for 3rd coord we couldnt find anything and the rest of the 9 options for 2nd coord had to then be redone and if still still 3 doesnt find a value, we'll have to backtrack and test rest of 9 values of 1st coord. Thus 9 values for 1st coord is where each time 2nd coord's 9 values had to be checked and thus going forward with rest of the coords too. So this is like 9(9(9....)) hence 9^nm. Additionally, each time in 9^nm we're also calling validate function which runs 2 for loop which runs for 9 times. Thus total TC = (9^2)(9^nm) => 9^(nm+2). Generalized as 9^nm.
# SC: O(mn) Explanation: Max length of recursive chain will be where at each col of every row, a new recursive call sets in. Which will go on and have a length of m*n recursive calls.