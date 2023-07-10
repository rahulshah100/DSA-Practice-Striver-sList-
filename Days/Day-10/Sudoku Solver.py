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
# Approach1: We'll traverse every row and in that every col, starting from 1st row 1st col i.e. index=0,0. If given col already has a value that is it is not "." we go to next column directly. Thus running out on all the cols will make us put a recursive call onto the function with incremented row, wherein again from 0th column we will traverse. Base condition is where in the function we discover row to be 9, that means we've been able to have all rows filled. While traversing a row and upon finding an empty column we'll iterate all values from 1 to 9 and see if any of them could be accomodated there. If so, we'll place that value for currRow and currColumn in the currBoard. But here finding one fitting value wont mean there could not be any other suitable values too. So to iterate over all possible solutions, at this spot we call a recursive function call with incremented column which will lead us forward with this value at currCol whereas the present for loop would keep checking for the remaining items at the same spot to be suitable. With recursive calls as they execute further either going down we'll encounter a situation where none of the items could be suitable for upcoming vacant spots or we'll traverse all the way through and hit the base condition. In case none of the items could fit we return false, and where we hit base case we return the currBoard. And as we're only asked one solution through constraints, so wherever we are putting a recursive calls we'll put an if-condition to see if returned value is array or a false. If array we'll return the currBoard, if false, we'll do nothing so further iterations could continue.
from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def helperFunc(row, col, currBoard):
            if row == 9: return currBoard

            for currCol in range(col, 9): #cheking all columns in currentRow
                if currBoard[row][currCol]!=".": continue
                for item in range(1, 10): #for a given empty column trying out all possible values
                    if check(row, currCol, item, currBoard):
                        currBoard[row][currCol] = str(item)
                        if helperFunc(row, currCol + 1, currBoard):  # --1  #In case value matched we put it at this index and start checking for next cols
                            return currBoard
                        currBoard[row][currCol] = "."  # So that in case where #--1 went to next call with 4,7 (row,col) where it could put 8 and #--1 got further called from there to find no matching cases for 4,4. So whe 4,4 comes back to 4,7 that's where at 4,7 next item is checked i.e. 9 and it didnt pass. So we go back to 4,7's parent say 4,6 now to check next item at 4,6 but here's where now we'll already have a 9 at 4,7 which will change the currBoard going forward.
                return False #If none of items matched for any empty row col, no solution with this arrangement
            if helperFunc(row + 1, 0, currBoard): # where function call receives column to be 10 i.e. prior row has been entirely traversed
                return currBoard

        return helperFunc(0, 0, board)


def check(currRow, currCol, item, board):
    for i in range(0,9):
        # check row
        if board[currRow][i]==str(item): return False
        # check col
        if board[i][currCol]==str(item): return False
        # check for that 3*3 unit where currRow, currCol belongs
        if board[(3*(currRow//3)) + (i//3)][(3*(currCol//3)) + (i%3)]==str(item): return False #Translating i=5 and currRow, currCol= 7, 3: 7//3=>2 shows second unit vertically (starting from 0,1,2). Each unit is 3 rows so to get an overall starting index of row=>2(3)=>6 shows current Row; Similarly 3//3=> 1 shows 1st unit horizontally out of 0,1,2. Each unit is 3 columns so 1(3)=3 shows current Col. Incorporating the current i count. 5//3=>1 shows row count out of 0,1,2 in current unit. 5%3=>2 shows col count out of 0,1,2 in current unit.
    return True

S = Solution()
print(S.solveSudoku([["5", "3", ".", ".", "7", ".", ".", ".", "."],
                     ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                     [".", "9", "8", ".", ".", ".", ".", "6", "."],
                     ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                     ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                     ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                     [".", "6", ".", ".", ".", ".", "2", "8", "."],
                     [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                     [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))
# TC: O(n(9^(nm))) Explanation: Here we have 9 possible items that could be checked for 1 index. Further each of those 9 possibilities will offer to choose for 9 more times so it is like 9(9(9...) given such n*m items in total we'll have 9(9(.. for length of n*m also meaning it could be written as 9^(nm) is time for all recursive calls. Further in each call we have a check function utilizing a for loop adding to n complexity for each of 9^(nm) recursive calls so total TC becomes n(9^(nm))
# SC: O(mn) Explanation: Max length of recursive chain will be where at each col of every row, a new recursive call sets in. Which will go on and have a length of m*n recursive calls.