#https://www.geeksforgeeks.org/problems/count-possible-ways-to-construct-buildings5007/1


class Solution:
	def TotalWays(self, N):
		# Code here
		a,b = 1,1
        mod = 10**9 + 7
        for i in range(1,N+1):
            a,b = b%mod, (a%mod + b%mod)%mod
        return (b**2) % mod
