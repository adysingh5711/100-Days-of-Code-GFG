#https://www.geeksforgeeks.org/problems/search-pattern0205/1


class Solution:
    def search(self, pat, txt):
        # code here
        dist = []
        p = len(pat)
        n = len(txt) - len(pat)
        for i in range(n+1):
            m = txt[i:i+p]
            if(m == pat):
                dist.append(i+1)
    
        return dist
