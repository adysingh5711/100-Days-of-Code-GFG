#https://www.geeksforgeeks.org/problems/largest-sum-subarray-of-size-at-least-k3121/1


class Solution():
    def maxSumWithK(self, a, n, k):
        # Code here
        max_sum = [0] * n
        # using kadane's algorithm
        max_sum[0] = a[0]
        
        for i in range(n):
            max_sum[i] = max(a[i], max_sum[i - 1] + a[i])
            
        _sum = 0
        for i in range(k):
            _sum += a[i]
        
        ans = _sum
        
        for i in range(k, n):
            _sum = _sum + a[i] - a[i - k]
            ans = max(ans, _sum)
            ans = max(ans, _sum + max_sum[i - k])
        
        return ans
