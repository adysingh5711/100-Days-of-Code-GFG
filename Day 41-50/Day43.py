#https://www.geeksforgeeks.org/problems/reverse-first-k-elements-of-queue/1


#Function to reverse first k elements of a queue.
class Solution:
    def modifyQueue(self, q, k):
        # code here
        return q[-1*(len(q)-k+1)::-1] + q[k:]
