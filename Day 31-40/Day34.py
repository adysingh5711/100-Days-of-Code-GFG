#https://www.geeksforgeeks.org/problems/smallest-window-containing-0-1-and-2--170637/1


class Solution:
    def smallestSubstring(self, S):
        # Code here
        # initialization
        i=0
        j=3
        res=-1
        
        # main loop with index updates
        while j<=len(S):
            st=S[i:j]
            if ("0" in st) and ("1" in st) and ("2" in st):
                if res==-1:
                    res=len(st)
                else:
                    res=min(res,len(st))
                i+=1
            else:
                j+=1
        
        return res
