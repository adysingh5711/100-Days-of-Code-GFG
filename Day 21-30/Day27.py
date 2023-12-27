#https://www.geeksforgeeks.org/problems/print-diagonally1623/1


class Solution:
    def antiDiagonalPattern(self,matrix):
        # Code here
        n = len(matrix)
        m = len(matrix[0])
        col = 0
        row = 0
        solution  = []
        while col < m and row < n:
            i = col
            j = row
            while i>=0 and j < n:
                solution.append(matrix[j][i])
                i -= 1
                j += 1
            if col < m - 1:
                col += 1
            else:
                row +=1
        return solution
