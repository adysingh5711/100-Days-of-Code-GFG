#https://www.geeksforgeeks.org/problems/count-of-strings-that-can-be-formed-using-a-b-and-c-under-given-constraints1135/1


class Solution:

    def countStr(self, n):
        # code here
        sumi = 0
        # Just a
        sumi += 1
        # one b or one c
        sumi += n + n
        # one b and one c
        sumi += n * (n - 1)
        # two c
        sumi += n * (n - 1) // 2
        # one b and two c
        sumi += n * (n - 1) * (n - 2) // 2
        return sumi
