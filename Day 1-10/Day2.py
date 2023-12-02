#https://www.geeksforgeeks.org/problems/inorder-traversal-and-bst5855/

class Solution:
    def isRepresentingBST(self, arr, N):
        # code here
        for i in range(N):
            if arr[i]==arr[-1]:
                break
            if arr[i]>arr[i+1]:
                return 0
        return 1
