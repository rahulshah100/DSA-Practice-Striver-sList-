# Problem: Pascal's Triangle
# LeetCode Link: https://leetcode.com/problems/pascals-triangle/

# Description: Given an integer numRows, return the first numRows of Pascal's triangle. In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

# Constraints: 1 <= numRows <= 30

# Examples: Input: numRows = 5 Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
#           Input: numRows = 1 Output: [[1]]
# -------------------------------------------------------------------------------


# Approach1:
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        PascalTri = [[1]]
        # Pascal Triangle is above initiated with 1 row already. Hence to make it have total numRows we will add further numRows-1 rows into it.
        for i in range(0, numRows - 1):
            # From the lastRow in PascalTriangle, we will keep deriving newRows and will keep appending them into Pascal Triangle.
            lastRow = PascalTri[-1]
            newRow = []
            # New Row will have one more item than the lastRow, hence below we run for loop for 0 to len(Row)+1 times.
            for j in range(0, len(lastRow) + 1):
                # For first and last item of the newRow we'll put 1 directly.
                if j == 0 or j == len(lastRow):
                    newRow.append(1)
                # For items apart from first and last items in a newRow, we'll compute them as below.
                else:
                    newRow.append(lastRow[j] + lastRow[j - 1])
            PascalTri.append(newRow)
        return PascalTri


S = Solution()
print(S.generate(5))
# print(S.generate(1))

# Time Complexity:O(n*((n+1)/2)) taking numRows as n. Explaination: Consider an example with n=5. When the first for loop runs for the first time we have inner for loop run for 0,1 i.e. 2 times. When first for loop runs for second time we have inner for loop run for 0,1,2 i.e. 3 times and so on upto last time the first for loop would be running for n-1th time and the inner for loop would run for 0,1,2,...n i.e. n times; this total iterations could be represented in formula as (n(n+1)/2)-1. We did -1 as for the first time we started directly with inner for loop running for 0,1 i.e. 2 items; if it was from 1 item upto n item then their summation would be n(n+1)/2, but we ignore 1 here as constant in our final answer. Proof of using this formula is the answer we get here by putting n=5; we'd get answer=[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]; in our formula by putting 5 we get 5(6/2) i.e. 15 which as we can see are total number of values in the obtained answer. If we put n=4 we'll get [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]] which are equal to 4(5/2)=10 number of items. Note:So if total n iterations are there and they are going like in the first iteration there is a further 1 iteration, then in 2nd iteration further 2 iterations... upto n iterations in the nth time then in total their iteration counts could be said as n(n+1)/2.
# Space Complexity:O(n^2) taking numRows as n. Explanation: at worst case i.e. during the last iteration lastRow would have n-1 items, newRow would have n items & PascalTriangle would have n(n+1)/2 items i.e. in total n(n+1)/2 as that entity dominates the other two. n(n+1)/2 could be generalized and written as n^2/2 + n/2 out of which n^2/2 dominates the equation and for a substantially bigger n value we can generalise the space required as n^2.
