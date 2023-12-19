# https://leetcode.com/problems/unique-paths/

# There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e. grid[0][0]). The robot tries to move to the bottom-right corner (i.e. grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.
# Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.
# The test cases are generated so that the answer will be less than or equal to 2 * 10^9.

# Example 1:
# Input: m = 3, n = 7
# Output: 28

# Example 2:
# Input: m = 3, n = 2
# Output: 3
# Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
# 1. Right -> Down -> Down
# 2. Down -> Down -> Right
# 3. Down -> Right -> Down

# Constraints:
# 1 <= m, n <= 100
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Approach1: Recursive Calls. Check for row, col+1 and row+1, col index; if that is the destination index, then return 1 as an addition in the ways found. If row,col+1 or row+1,col exceeds the max row or columns given in the provided array then return 0. Else, make a further recursive call to row,col+1 and row+1,col. Keep summing up the results of recursive calls of row,col+1 and row+1,col so to get the count of total ways where destination is met.
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return self.helper(0, 0, m, n)

    def helper(self, currRow, currCol, totRows, totCols):
        if currRow == totRows - 1 and currCol == totCols - 1:
            return 1
        elif 0 <= currRow < totRows and 0 <= currCol < totCols:
            return (self.helper(currRow + 1, currCol, totRows, totCols) + self.helper(currRow, currCol + 1, totRows, totCols))
        else:
            return 0


S = Solution()
print(S.uniquePaths(3, 2))
# Time Complexity: O(2^mn). Explanation: Each time helper function is executed there are two more executions of it that springs. In total we can count we'll be traversing through each block of given matrix and as such there'll be m*n blocks, we get 2 executions, 2 executions... for m*n times i.e. 2^(m*n) is rate by which algo expands.
# Note this case is totally different than merge sort, but the recursive tree formation could be confused being similar. In mergersort we have a whole array constrained from left to right which keeps being reduced to half, half... for n times. Unlike that here we start from one point which is not at all concise coz we then go on expanding uptill a bar is met. Hence, whereas mergesort's recursion is a converging triangle from top to bottom, this one is a flip to that i.e. from top to bottom an ever expanding triangle.
# Space Complexity: O(m+n). Explanation: Alogrithmic Space = O(1) and Stack/Recursive Space = O(m+n) So total=O(m+n). At max for any call, when our we're at the farthest i.e.m,nth point, the stack space would be only keeping in memory the chain of recursion calls leading upto this one which at worst could be m+n calls. Note: for storing recursion call if there is a chain of calls, then only one active/recent call consumes algorithmic space while the others would be collapsed and would use O(1) Space; that's how recursion is implemented on the backside of code.


# Approach2: Better time, worsened space complexity. Instead of computing for each coordinate everytime, we can use precomputized value by storing it in the hashtable when the first time that coordinate was computed. Thus at max we'll just have to compute all coordinates once and there being n*m coordinates/items, we'll have our time complexity reduced to n*m.
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return helper(0, 0, m, n, {}) #--1

def helper(currRow, currCol, totRows, totCols, hashDict): # Notice how compared to actual params (--1) the formal params uses different varName. This is necessary, because List and some data types are mutable and so just one copy of such actual params are stored which could be overwritten at untimely manner by formal params. So remember to use different name of arguments and parameters.
    if currRow == totRows - 1 and currCol == totCols - 1:
        return 1
    elif (currRow, currCol) in hashDict:  # As Lists are mutable, they are not allowed to be keys, and hence I have used tuples as dictionary's key
        return hashDict[(currRow, currCol)]
    elif 0 <= currRow < totRows and 0 <= currCol < totCols:
        hashDict[(currRow, currCol)] = helper(currRow + 1, currCol, totRows, totCols, hashDict) + helper(
            currRow, currCol + 1, totRows, totCols, hashDict)
        return hashDict[(currRow, currCol)]
    else:
        return 0


S = Solution()
print(S.uniquePaths(3, 2))
# Time Complexity: O(nm). Explaination: At max only for all the coordinates we'd have to compute once and the rest could just be looked up from there.
# Space Complexity: O(nm+n+m). Explanation: nm space for hashmap and n+m for stack space to store recursive call chain.


# Approach3: Better space and time complexity. Here we have observed that for an m*n matrix to reach at (m-1)*(n-1)th index from 0th index, we've always had to take n-1 rights and m-1 downs. For eg: in 3*4 matrix i.e. rows=3 and cols=4, to reach from 0,0th index to the last index i.e.2,3rd index we'll certainly have to take 3 Rights & 2 Downs. As we notice further we can figure that all the permutation and combination of n-1 rights and m-1 downs would make us reach the destination. Eg continuing the 3 rows 4 columns example from above, we have total n-1+m-1 direction to take i.e. 5 directions so we make 5 '_' as: _ _ _ _ _ . We can make them R R D D D or D R D D D R and they'll all make us reach the destination. So now the total way to find has become a permutation combination problem. We can either find that in 5 '_' what are possible ways to arrange all the R's as counter to which the D's will get adjusted or we can do vice versa. I have decided to find R's combination and so we'll find ((n-1)+(m-1))C(n-1). Formula for 10C3 would be 10*9*8/1*2*3. 10C3 would mean number of possible arrangements for choosing a total of 3 places out of 10.
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # nCr = (n-1 + m-1)C(n-1)
        N = m + n - 2
        R = m - 1
        Nact = 1
        Ract = 1
        for i in range(0, R):
            Nact *= N - i
            Ract *= R - i
        return Nact // Ract


S = Solution()
print(S.uniquePaths(3, 2))
# Time Complexity:O(m). Explanation: for loop runs for m-1 times. Thus O(m-1) is our time complexity, generalized as O(m).
# Space Complexity: O(1)
