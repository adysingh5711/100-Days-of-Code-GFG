# https://www.geeksforgeeks.org/problems/sorted-insert-for-circular-linked-list/1


'''
class Node: 
    # Constructor to initialize the node object 
    def __init__(self, data): 
        self.data = data 
        self.next = None
  '''
class Solution:
    def sortedInsert(self, head, data):
        new_node = Node(data)

        # Case: Empty linked list
        if not head:
            new_node.next = new_node
            return new_node

        current = head

        # Case: Insert at the beginning
        if data < head.data:
            while current.next != head:
                current = current.next
            current.next = new_node
            new_node.next = head
            return new_node

        # Case: Insert in the middle or at the end
        while current.next != head and current.next.data < data:
            current = current.next

        new_node.next = current.next
        current.next = new_node

        return head
