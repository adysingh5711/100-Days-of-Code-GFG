# https://www.geeksforgeeks.org/problems/subtraction-in-linked-list/1 


class Solution:
    def subLinkedList(self, l1, l2): 
        # Code here
        # return head of difference list
        temp1=l1
        temp2=l2
        s2=0
        s1=0
        while(temp1):
            s1=s1*10+temp1.data
            temp1=temp1.next
        while(temp2):
            s2=s2*10+temp2.data
            temp2=temp2.next
        t=Node(abs(s1-s2))
        return t
