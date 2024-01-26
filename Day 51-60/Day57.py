# https://www.geeksforgeeks.org/problems/fractional-knapsack-1587115620/1


class Item:
    def __init__(self,val,w):
        self.value = val
        self.weight = w
        
class Solution:    
    #Function to get the maximum total value in the knapsack.
    def fractionalknapsack(self, W,arr,n):
        
        # code here
        arr.sort(key=lambda x:x.value/x.weight,reverse=True)
        ans=0
        wt=0
        i=0
        while i<n and wt<W:
            if wt+arr[i].weight<=W:
                wt+=arr[i].weight
                ans+=arr[i].value
            else:
                ww=W-wt
                wt=W
                ans+=(arr[i].value/arr[i].weight)*ww
            i+=1
        return ans
