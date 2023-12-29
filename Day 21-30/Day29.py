#https://www.geeksforgeeks.org/problems/check-if-a-string-is-repetition-of-its-substring-of-k-length3302/1


from collections import Counter
class Solution:
    def kSubstrConcat(self, n, s, k):
        if n%k!=0:
            return 0
        l=[]
        for i in range(0,n,k):
            ele=s[i]
            for j in range(1,k):
                ele+=s[i+j]
            l.append(ele)
        d=Counter(l)
        if len(d)>2:
            return 0
        count=0
        for i in d:
            if d[i]>1:
                count+=1
        if count==2:
            return 0
        return 1
