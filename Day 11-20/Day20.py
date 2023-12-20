#https://www.geeksforgeeks.org/problems/variation-in-nim-game4317/1


class Solution:
    def findWinner(self, n, A):
        # code here
        res=0
        for i in A:
            res=res^i
        if (n&1==1 and res>0):
            return 2
        else:
            return 1
