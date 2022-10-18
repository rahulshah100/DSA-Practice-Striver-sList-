# https://leetcode.com/problems/unique-paths/

# There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e. grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.
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
# Approach1: Recursive Calls. Check for row,col+1 and row+1,col index if that is the destination index, then return 1 as an addition in the ways found. If row,col+1 or row+1,col exceeds the max row or columns given in the provided array then return 0. Else, make a further recursive call to row,col+1 and row+1,col. Keep summing up the results of recursive calls of row,col+1 and row+1,col so to get the count of total ways where destination is met.
from typing import List


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ways = Find(m - 1, n - 1, 0, 0)
        return ways


def Find(DestinationRow, DestinationCol, CurrRow, CurrCol):
    if CurrRow == DestinationRow and CurrCol == DestinationCol:
        return 1
    elif CurrRow <= DestinationRow and CurrCol <= DestinationCol:
        A = Find(DestinationRow, DestinationCol, CurrRow + 1, CurrCol)
        B = Find(DestinationRow, DestinationCol, CurrRow, CurrCol + 1)
        return A + B
    else:
        return 0


S = Solution()
print(S.uniquePaths(2, 3))
# Time Complexity: O(2^mn). Explaination: As with every time, there are 2 new executions being unfold, for having to do it 2 times, say initially we had one execution we call it in terms of item as- 0,0 then we'll have item1 (1,0) and item2 (0,1). Further from item 1 we'll have more 2 items 2,0 and 2,1 and from item2 we'll be having 1,1 and 0,2. In total, after doing it twice we'll have 4 items. This type of complexities are called exponential power.
# Note here unlike in merge sort, where although the recursive tree formation of solution looks the same, but in mergersort where if 8 was array size in 3 operations we'll be at single single elements as array was getting divided. Unlike that here, we'll need 2^8 as every time there are more possibilities to explore. Hence unlike logn our time complexity is 2^n.
# Space Complexity: O(mn). Explaination: At max at a point (point is when it is worst case for space memory usage), our stack space would be storing the recursion calls for all the items of array which will be mn. On top of that no other extra variable is used to store anything, so in total thus, mn space is required.


# Approach2: Better time complexity, worsened space complexity. Instead of having to compute for each coordinate everytime, if we can use precomputized value by storing it in the hashtable, when the first time that coordinate was computed, then at max we'll just have to compute all coordinates once and there being n*m coordinates/items, we'll have our time complexity reduced to being n*m.
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        TheHashTable=[[-1]*n]*m
        ways = Find(m - 1, n - 1, 0, 0, TheHashTable)
        return ways


def Find(DestinationRow, DestinationCol, CurrRow, CurrCol, Hashtable):      #Remember to use a different name as arguement in the function than was in the parameter where function was called. Here I saw a bad flaw when I used TheHashTable instead of HashTable. I saw flaw Because List is mutable, I think just one copy of list was stored which is TheHashTable that is declared in the uniquePaths and that was being overwrote at untimely manner in the function Find. So remember to use different name of arguements and parameters.
    if CurrRow == DestinationRow and CurrCol == DestinationCol:
        return 1
    elif CurrRow <= DestinationRow and CurrCol <= DestinationCol:
        A = Find(DestinationRow, DestinationCol, CurrRow + 1, CurrCol, Hashtable)
        B = Find(DestinationRow, DestinationCol, CurrRow, CurrCol + 1, Hashtable)
        return A + B
    else:
        return 0


S = Solution()
print( S.uniquePaths(2, 3))
# Time Complexity: O(nm). Explaination: At max only for all the coordinates we'd have to compute once and the rest could just rereference from there/
# Space Complexity: O(2nm). Explaination: nm space for hashmap and nm space for storing worst case recursive calls which'd be nm.


# Approach3: Better space and time complexity. Here we have observed that for an m*n matrix to reach at (m-1)*(n-1)th index from 0th index, we'd always have to take n-1 rights and m-1 downs. For eg: in 3*4 matrix i.e. rows=3 and cols=4, to reach from 0,0th index to the last index i.e.2*3rd index we'll have certainly have to take 3 Rights & 2 Downs. As we notice further we can figure that all the permutation and combination of n-1 rights and m-1 downs would make us reach the destination. Eg continuing the above 3*4 exampel we have total n-1+m-1 direction to take i.e. 5 directions so we make 5 _ as: _ _ _ _ _ . We can make them R R D D D or D R D D D R and they'll all make us reach the destination. So now the total way to find has become a permutation combination problem. We can either find that in 5 _ what are possible ways to arrang all the R's as counter to that the D's will get adjusted or we can do vice versa. I have decided to find R's combination and so we'll find ((n-1)+(m-1))C(n-1). Formula for 10C3 would be 10*9*8/1*2*3.
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m==1 or n==1:           #If it is m*1 or 1*n matrix then only one path is possible.
            return 1
        else:
            Top = n-1 + m-1
            interim = Top
            Bottom = 1
            for i in range(2,n):
                interim=interim-1
                Top = Top*interim
                Bottom = Bottom * (i)
            return Top//Bottom
S = Solution()
print(S.uniquePaths(3, 7))
# print(S.uniquePaths(10, 1))
# Time Complexity:O(n). Explaination: for loop will loop from 2 to n-1 i.e n-2 times. Thus O(n-2) is our time complexity, generalized as O(n).
# Space Complexity: O(1)