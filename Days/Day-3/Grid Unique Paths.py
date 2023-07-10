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
from typing import List


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return helperFunc(m - 1, n - 1, 0, 0)


def helperFunc(DestinationRow, DestinationCol, CurrRow, CurrCol):
    if CurrRow == DestinationRow and CurrCol == DestinationCol:
        return 1
    elif CurrRow <= DestinationRow and CurrCol <= DestinationCol:
        A = helperFunc(DestinationRow, DestinationCol, CurrRow + 1, CurrCol)
        B = helperFunc(DestinationRow, DestinationCol, CurrRow, CurrCol + 1)
        return A + B
    return 0


S = Solution()
print(S.uniquePaths(2, 3))


# Time Complexity: O(2^mn). Explanation: As with every time, there are 2 new executions being unfold, And having mn total elem we get the stated TC.
# Note this case is totally different than merge sort, but the recursive tree formation could be confused being similar. In mergersort we have a whole array constrained from left to right and that is being reduced half half i.e. for n times. Unlike that here we start from one point which is not at all concise coz we then go on expanding uptill a bar is met. Hence whereas mergesort's recursion is a converging triangle from top to bottom, this one is a flip to that i.e. from top to bottom an ever expanding triangle.
# Space Complexity: O(mn). Explaination: Alogrithmic Space = O(1) and Recursion Space = O(mn) So total=O(mn). At max at a point (point is when it is worst case for space memory usage) our stack space would store the recursion calls for all the items of array. Note: for storing recursion call if there is a chain of calls, then only one active/recent call consumes algorithmic space while the others would be collapsed and would use O(1) Space; that's how recursion is implemented on the backside of code. Hence at a time if all mn items of given grids are running then in such worst case, space complexity will be mn. On top of that no other extra variable is used to store anything, so in total thus mn space is required if we consider stack space for function calls, otherwise it is O(1).


# Approach2: Better time complexity, worsened space complexity. Instead of having to compute for each coordinate everytime, if we can use precomputized value by storing it in the hashtable, when the first time that coordinate was computed, then at max we'll just have to compute all coordinates once and there being n*m coordinates/items, we'll have our time complexity reduced to being n*m.
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return helperFunc(0, 0, m, n, {})


def helperFunc(r, c, tm, tn,
               hashmap):  # Notice how compared to uniquePaths' helperFunc call, here at function declaration I used different varName. This is necessary, because List and some data types are mutable, just one copy of them are stored that is declared in the parent i.e. uniquePaths and that could be overwrote at untimely manner in the function declaration. So remember to use different name of arguments and parameters.
    if r == tm - 1 and c == tn - 1:
        return 1
    elif r < tm and c < tn:
        if (r,
            c) in hashmap:  # As Lists are mutable, they are not allowed to be keys, and hence I have used tuples as dictionary's key
            return hashmap[(r, c)]
        else:
            L = helperFunc(r + 1, c, tm, tn, hashmap)
            R = helperFunc(r, c + 1, tm, tn, hashmap)
            hashmap[(r, c)] = L + R
            return L + R
    return 0


S = Solution()
print(S.uniquePaths(3, 7))


# Time Complexity: O(nm). Explaination: At max only for all the coordinates we'd have to compute once and the rest could just be looked up from there.
# Space Complexity: O(2nm). Explaination: nm space for hashmap and nm space for storing worst case recursive calls which'd be nm. So total=2nm.


# Approach3: Better space and time complexity. Here we have observed that for an m*n matrix to reach at (m-1)*(n-1)th index from 0th index, we've always had to take n-1 rights and m-1 downs. For eg: in 3*4 matrix i.e. rows=3 and cols=4, to reach from 0,0th index to the last index i.e.2,3rd index we'll certainly have to take 3 Rights & 2 Downs. As we notice further we can figure that all the permutation and combination of n-1 rights and m-1 downs would make us reach the destination. Eg continuing the 3 rows 4 columns example from above, we have total n-1+m-1 direction to take i.e. 5 directions so we make 5 '_' as: _ _ _ _ _ . We can make them R R D D D or D R D D D R and they'll all make us reach the destination. So now the total way to find has become a permutation combination problem. We can either find that in 5 '_' what are possible ways to arrange all the R's as counter to that the D's will get adjusted or we can do vice versa. I have decided to find R's combination and so we'll find ((n-1)+(m-1))C(n-1). Formula for 10C3 would be 10*9*8/1*2*3. 10C3 would mean number of possible arrangements for choosing a total of 3 places out of 10.
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # nCr = (n-1 + m-1)C(n-1)
        denom, currDenom = 1, n - 1
        numer, currNumer = 1, n + m - 2
        while currDenom > 0:
            denom *= currDenom
            currDenom -= 1
            numer *= currNumer
            currNumer -= 1
        return numer // denom


S = Solution()
print(S.uniquePaths(3, 7))

# Time Complexity:O(n). Explaination: while loop will loop for n-1 times. Thus O(n-1) is our time complexity, generalized as O(n).
# Space Complexity: O(1)
