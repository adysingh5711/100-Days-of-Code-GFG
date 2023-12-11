#https://www.geeksforgeeks.org/problems/max-sum-subarray-of-size-k5313/1

class Solution:
    def maximumSumSubarray (self,K,Arr,N):
        # code here 
        max_sum=-1
        cs=0
        for i in range(K):
            cs+=Arr[i]
        left=0
        right=K-1
        l=[]
        while right<N:
            l.append(cs)
            cs-=Arr[left]
            left+=1
            right+=1
            if right<N:
                cs+=Arr[right]
        return max(l)
