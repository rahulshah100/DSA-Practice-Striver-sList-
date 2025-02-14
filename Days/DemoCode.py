from typing import List






class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rowSet,colSet=set(),set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    rowSet.add(i)
                    colSet.add(j)

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in rowSet:
                    matrix[i][j]=0
                elif j in colSet:
                    matrix[i][j]=0

        return matrix









S=Solution()
print(S.setZeroes([[1,1,1],[1,0,1],[1,1,1]]))