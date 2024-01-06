#https://www.geeksforgeeks.org/problems/split-array-largest-sum--141634/1


class Solution:
    def splitArray(self, arr, N, K):
        # code here 
        l, r = max(arr), sum(arr)
        while l < r:
            mid = (l + r) // 2
            cursum, count = 0, 0
            for num in arr:
                cursum += num
                if cursum > mid:
                    cursum = num
                    count += 1
            if count >= K: l = mid + 1
            else: r = mid
        return r
