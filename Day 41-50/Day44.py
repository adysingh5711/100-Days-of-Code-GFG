# https://www.geeksforgeeks.org/problems/insertion-sort-for-singly-linked-list/1


'''
# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''

class Solution:
    def insertionSort(self, head):
        #code here
        curr_i=head.next
        prev_i=head
        while curr_i:
            curr_j=head
            if head.data>curr_i.data:
                prev_i.next=curr_i.next
                curr_i.next=head
                head=curr_i
            else:
                while curr_j.next.data<curr_i.data:
                    curr_j=curr_j.next
                if curr_j!=prev_i:
                    prev_i.next=curr_i.next
                    curr_i.next=curr_j.next
                    curr_j.next=curr_i
                else:
                    prev_i=curr_i
            curr_i=prev_i.next
        return head
