# https://www.geeksforgeeks.org/problems/longest-repeating-and-non-overlapping-substring3421/1


class Solution:
    def longestSubstring(self, s , n):
        # code here 
        max_len=0
        end=-1
        dp=[[0]*(n+1) for _ in range(n+1)]
        for i in range(n):
            for j in range(i+1,n):
                if s[i]==s[j] and j-i>dp[i][j]:
                    dp[i+1][j+1]=1+dp[i][j]
                    if dp[i+1][j+1]>max_len:
                        max_len=dp[i+1][j+1]
                        end=i
        if end==-1:
            return "-1"
        return s[end-max_len+1:end+1]
