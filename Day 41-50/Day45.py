#https://www.geeksforgeeks.org/problems/find-duplicate-rows-in-a-binary-matrix/1


class Solution:
    def repeatedRows(self, arr, m ,n):
        #code here
        st = set()
        ans = []
        ind = 0
        
        for i in arr:
            curr = tuple(i)
            if curr in st: ans.append(ind)
            else: st.add(curr)
            ind += 1   
        
        return ans  
