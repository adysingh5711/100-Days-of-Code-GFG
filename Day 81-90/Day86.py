# https://www.geeksforgeeks.org/problems/maximum-sum-problem2211/1


class Solution:
    def maxSum(self, n): 
        # code here 
        if n<12:
            return int(n)
        return int(self.maxSum(n/2)+self.maxSum(n/3)+self.maxSum(n/4))
