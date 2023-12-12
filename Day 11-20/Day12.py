#https://www.geeksforgeeks.org/problems/gold-mine-problem2608/1

class Solution:
    def maxGold(self, n, m, M):
        # code here
        for col in range(m-2,-1,-1):
            for row in range(0,n):
                right=M[row][col+1]
                if row==0:
                    right_row=0
                else:
                    right_row=M[row-1][col+1]
                if row==n-1:
                    right_down=0
                else:
                    right_down=M[row+1][col+1]
                M[row][col]+=max(right,right_row,right_down)
        res=M[0][0]
        for i in range(n):
            res=max(res,M[i][0])
        return res
