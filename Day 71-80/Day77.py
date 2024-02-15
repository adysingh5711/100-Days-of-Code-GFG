# https://www.geeksforgeeks.org/problems/castle-run3644/1


class Solution:
    def isPossible(self, paths):
        # Code here
        for row in paths:
            sum = 0
            for col in row:
                sum = sum + col
            if sum%2 != 0:
                return 0
        return 1
