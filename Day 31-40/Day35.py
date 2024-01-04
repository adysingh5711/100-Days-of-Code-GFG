#https://www.geeksforgeeks.org/problems/find-element-occuring-once-when-all-other-are-present-thrice/1


class Solution:
    def singleElement(self, arr, N):
        # code here 
        return ((sum(set(arr))*3)-sum(arr))//2
