#https://www.geeksforgeeks.org/problems/game-of-xor1541/1


class Solution:
    def gameOfXor(self, N , A):
        # code here 
        ans=0
        for i,v in enumerate(A):
            if (i+1)*(N-i)%2==1:
                ans^=v
        return ans
