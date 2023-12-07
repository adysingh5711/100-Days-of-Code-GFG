#https://www.geeksforgeeks.org/problems/number-of-subarrays-with-maximum-values-in-given-range5949/1

class Solution:
    def countSubarrays(self, a,n,L,R): 
        # Complete the function
        left=0
        right = 0
        count = 0
        position = 0
        while right < len(a):
            if a[right] > R:
                position = 0
                left = right+1
            elif a[right] <=R and a[right] >= L:
                position = right-left+1
                count = count + position
            elif a[right]<L:
                count = count + position
            right = right + 1
        return count
