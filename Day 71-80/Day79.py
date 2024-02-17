# https://www.geeksforgeeks.org/problems/does-array-represent-heap4345/1


class Solution:
    def isMaxHeap(self,arr,n):
        # Your code goes here   
        for i in range(1, n):
            parent = (i + 1) // 2
            if arr[parent - 1] < arr[i]:
                return False
                
        return True
