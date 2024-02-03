'''
class node:
    def __init__(self):
        self.data = None
        self.next = None
'''

class Solution:
    def decimalValue(self, head):
        MOD = 10**9+7
        # Code here
        res = ""
        
        while head:
            res += str(head.data)
            head = head.next
            
        res = int(res, 2)
        res %= MOD
            
        return res
