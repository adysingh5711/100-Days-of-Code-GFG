#https://www.geeksforgeeks.org/problems/reach-the-nth-point5433/1


class Solution:
	def nthPoint(self,n):
		# Code here
		mod=(10**9)+7
        fib=[0]*(n+1)
        fib[0]=1
        fib[1]=1
        for i in range(2,n+1):
            fib[i]=(fib[i-1]+fib[i-2])%mod
        return fib[n]
