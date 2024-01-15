#https://www.geeksforgeeks.org/problems/grinding-geek/1


from typing import List


class Solution:
    def max_courses(self, n : int, total : int, cost : List[int]) -> int:
        # code here
        from math import floor
        
        dp = [[None]*len(cost) for _ in range(total+1)]
        
        def compute(i, total):
            nonlocal cost, n, dp
            if i >= len(cost):
                return 0
            if dp[total][i] is not None:
                return dp[total][i]
            c1 = compute(i+1, total)
            
            if total < cost[i]:
                dp[total][i] = c1
                return c1
                
            rcost = cost[i]
            if i < n:
                rcost -= floor(cost[i]*0.9)

            dp[total][i] =  max(c1, compute(i+1, total-rcost)+1)
            return dp[total][i]
        
        return compute(0, total)
