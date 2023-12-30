#https://www.geeksforgeeks.org/problems/winner-of-an-election-where-votes-are-represented-as-candidate-names-1587115621/1


from collections import Counter
class Solution:
    
    #Complete this function
    
    #Function to return the name of candidate that received maximum votes.
    def winner(self,arr,n):
        # Your code here
        # return the name of the winning candidate and the votes he recieved
        data = dict(Counter(arr))
        winner = max(data.values())
        for ele in sorted(data.keys()):
            if data[ele] == winner:
                return [ele , winner]
