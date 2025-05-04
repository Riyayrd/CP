###https://leetcode.com/problems/set-matrix-zeroes/

### https://www.youtube.com/watch?v=N0MgLvceX7M
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #BETTER 2 Space complexity O(1)
        #Consider row and columns of matrix as storage markers and then traverse the lower section first and then the upper mattrix
        #BETTER 1
        row=[]
        col=[]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    row.append(i)
                    col.append(j)
        for i in row:
            for j in range(len(matrix[0])):
                matrix[i][j]=0
        for i in col:
            for j in range(len(matrix)):
                matrix[j][i]=0

        #BRUTE FORCE 
        # for i in range(len(matrix)):
        #     for j in range(len(matrix[0])):
        #         if matrix[i][j]==0:
        #             for k in range(len(matrix)):
        #                 if matrix[k][j]!=0:
        #                     matrix[k][j]=-1
        #             for m in range(len(matrix[0])):
        #                 if matrix[i][m]!=0:
        #                     matrix[i][m]=-1


        # for i in range(len(matrix)):
        #     for j in range(len(matrix[0])):
        #         if matrix[i][j]==-1:
        #             matrix[i][j]=0

        
