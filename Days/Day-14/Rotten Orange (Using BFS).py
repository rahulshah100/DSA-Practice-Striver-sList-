# https://leetcode.com/problems/rotting-oranges/

# You are given an m x n grid where each cell can have one of three values:
# 0 representing an empty cell,
# 1 representing a fresh orange, or
# 2 representing a rotten orange.
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.
# Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

# Example1:
# Input: grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
# Output: 4

# Example2:
# Input: grid = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
# Output: -1
# Explanation: The orange in the bottom left corner(row 2, column 0) is never rotten, because rotting only happens 4 - directionally.

# Example 3:
# Input: grid = [[0, 2]]
# Output: 0
# Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.

# Constraints:
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 10
# grid[i][j] is 0, 1, or 2.
# -------------------------------------------------------------------------------------------------------------------------------------------
# Approach1: As we can see that by default for all the 2s in grid, we want to first change all their adjacents into rotten and then go further in each of them to do the same, we understand this to be a Breadth First Search and not a Depth First Search. In DFS we use a stack as it only keeps popping the top item, and so there we'll first go deeper into first 2 we find and keep going further like that instead of covering the whole same level at first, but unlike that because we use BFS here, we'll use a Queue here because it pops the base thus always ensuring the same level to be covered first. So we use a tempQ to store coordinates of items where we find 2 in the grid. As we also want to find maxTime, we'll store a triplet of i, j (coords), currTime in queue. Further, we maintain a visitedMatr identical to given grid where we'll only have 0s. Now we first iterate whole grid and store all 2s already given. Then we run a while loop for uptill queue is not empty in which for given coords we'll check all 4 of its adjacents and if any arrangement becomes possible (for which we check that coord is in bounds of grid, then grid item at that index is 1 and also that visitedMatr at that index is 0) we mark visitedMatr as 1 at that index and store the identified coords along with currTime+1 as the new time in the queue. We'll also use a maxTime that keeps track of max currTime. After exhausting Queue we traverse given grid and wherever we see 1 we check in visitedMatr if that index has been visited and thus changed to 1, which if not the case we return -1. At the end we return maxTime.
from queue import Queue
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        visitedMatr = [[0 for col in grid[0]] for row in grid]
        tempQ = Queue()
        maxTime = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    tempQ.put((i, j, 0))

        while tempQ.queue:
            i, j, currTime = tempQ.get()
            if checkCoords(i + 1, j, len(grid), len(grid[0]), visitedMatr, grid):
                tempQ.put((i + 1, j, currTime+1))
            if checkCoords(i - 1, j, len(grid), len(grid[0]), visitedMatr, grid):
                tempQ.put((i - 1, j, currTime+1))
            if checkCoords(i, j + 1, len(grid), len(grid[0]), visitedMatr, grid):
                tempQ.put((i, j + 1, currTime+1))
            if checkCoords(i, j - 1, len(grid), len(grid[0]), visitedMatr, grid):
                tempQ.put((i, j - 1, currTime+1))
            maxTime = max(maxTime, currTime)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and visitedMatr[i][j]!=1:
                    return -1
        return maxTime


def checkCoords(i, j, rows, cols, visitedMatr, grid):
    if 0 <= i < rows and 0 <= j < cols and visitedMatr[i][j] == 0 and grid[i][j]==1:
        visitedMatr[i][j] = 1
        return True
    return False


S = Solution()
print(S.orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]))
print(S.orangesRotting([[0,2]]))
# TC: O(3*N*M) Explanation: N*M for first nested loop, then the while will take N*M and at last nested for-loop before returning maxTime, will take N*M more
# SC: O(2*N*M) Explanation: N*M to create visitedMatr and for a grid with all items as 2, queue will store at worst N*M entries