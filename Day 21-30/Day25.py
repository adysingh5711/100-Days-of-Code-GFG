#https://www.geeksforgeeks.org/problems/determinant-of-a-matrix-1587115620/1


    def determinantOfMatrix(self,matrix,n):
        # code here 
        if n==1:
            return matrix[0][0]
        if n==2:
            return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
        ans=0
        for i in range(n):
            mat=[matrix[j][1:] for j in range(n) if j!=i]
            ans+=((-1)**(i))*matrix[i][0]*self.determinantOfMatrix(mat,n-1)
        return ans
