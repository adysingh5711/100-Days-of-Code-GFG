#https://www.geeksforgeeks.org/problems/merge-2-sorted-linked-list-in-reverse-order/1


'''
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
'''

class Solution:
    def mergeResult(self, h1, h2):
        #return head of merged list
        if h1 is None and h2 is None:
            return None
        lis = []
        while h1:
            lis.append(h1.data)
            h1 = h1.next
        
        while h2:
            lis.append(h2.data)
            h2 = h2.next
            
        lis.sort()
        lis.reverse()
        root = Node(lis[0])
        cur = root
        
        for val in (lis[1:]):
            cur.next = Node(val)
            cur = cur.next
        return root
