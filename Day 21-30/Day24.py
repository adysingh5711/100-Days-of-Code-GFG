#https://www.geeksforgeeks.org/problems/buy-maximum-stocks-if-i-stocks-can-be-bought-on-i-th-day/1


from typing import List
class Solution:
    def buyMaximumProducts(self, n : int, k : int, price : List[int]) -> int:
        # code here
        l=[(i+1,price[i]) for i in range(n)]
        l.sort(key=lambda item:item[1])
        i,count=0,0
        while i<n and l[i][1]<=k:
            if k>=l[i][0]*l[i][1]:
                count+=l[i][0]
                k-=l[i][0]*l[i][1]
            else:
                count+=k//l[i][1]
                k%=l[i][1]
            i+=1
        return count
