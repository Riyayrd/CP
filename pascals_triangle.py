#https://leetcode.com/problems/pascals-triangle/

#https://youtu.be/bR7mQgwQ_o8


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
 
        #optimal 
        ans = []

        for row in range(1, numRows+1):
            ans_var = 1
            ansRow = [1]
            for col in range(1, row):
                ans_var *= (row - col)
                ans_var //= col
                ansRow.append(ans_var)
            ans.append(ansRow)
        return ans
        
        #BRUTE SOLUTION
        # if numRows==1:
        #     return [[1]]
        # a=[[]]*numRows
        # for i in range(numRows):
        #     a[i]=[1]*(i+1)
        #     for j in range(1,i):
        #         a[i][j]=a[i-1][j-1]+a[i-1][j]

        # return a
