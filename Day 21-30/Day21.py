#https://www.geeksforgeeks.org/problems/candy/1


class Solution:
    def minCandy(self, N, ratings):
        # Code here
        if N == 1:
            return 1
        candies  = [1 for i in range(N)]
        for i in range(1,N):
            # print(i)
            if ratings[i] > ratings[i-1] :
                candies[i] = max(candies[i],candies[i-1] + 1)
        for i in range(N-2, -1, -1):
            if ratings[i] > ratings[i+1] :
                candies[i] = max(candies[i], candies[i+1] + 1)
        return sum(candies)
