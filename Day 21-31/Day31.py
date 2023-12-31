#https://www.geeksforgeeks.org/problems/good-by-2023/1


from typing import List


class Solution:
    def isPossible(self, N : int, coins : List[int]) -> bool:
        # code here
        def helper(i,s):
            if s>0 and (s%20==0 or s%24==0 or s==2024):
                return True
            if i>=N:
                return False
            return helper(i+1,s+coins[i]) or helper(i+1,s)
        return helper(0,0)
