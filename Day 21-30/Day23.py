#https://www.geeksforgeeks.org/problems/count-element-occurences/1


class Solution:
    
    #Function to find all elements in array that appear more than n/k times.
    def countOccurence(self,arr,n,k):
        #Your code here
        d={}
        count=0
        for i in arr:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        for i,j in d.items():
            if j>n//k:
                count+=1
        return count
