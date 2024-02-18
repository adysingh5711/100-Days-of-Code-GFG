# https://www.geeksforgeeks.org/problems/sum-of-leaf-nodes-in-bst/1


'''
class Node:
    def __init__(self, data=0):
        self.data=0
        self.left=None
        self.right=None
'''

class Solution:
    def sumOfLeafNodes(self, root):
        if not root:
            return 0
        if not (root.left or root.right):
            return root.data
        a = self.sumOfLeafNodes(root.left)
        b = self.sumOfLeafNodes(root.right)
        return a+b
