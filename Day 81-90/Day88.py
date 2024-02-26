# https://www.geeksforgeeks.org/problems/power-set4302/1


#User function Template for python3

class Solution:
    def AllPossibleStrings(self, s):
        def fun(ind,sam):
            if ind==n:
                if sam:
                    # if sam is not empty append to the ans 
                    ans.append(sam)
                return 
            # include the character
            fun(ind+1,sam+s[ind])
            # exclude the character
            fun(ind+1,sam)
        n=len(s)
        ans=[]
        fun(0,"")#call the funtion fun
        ans.sort()#sorting lexographically 
        return ans 
