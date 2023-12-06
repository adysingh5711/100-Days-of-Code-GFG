#https://www.geeksforgeeks.org/problems/how-many-xs4514/1

class Solution:    
    def countX(self,L,R,X):
        #code here
        return sum([str(_).count(str(X)) for _ in range(L+1,R)])
