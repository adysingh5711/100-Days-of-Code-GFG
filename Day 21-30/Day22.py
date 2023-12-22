#https://www.geeksforgeeks.org/problems/maximum-meetings-in-one-room/1


class Solution:
    def maxMeetings(self, N : int, S : List[int], F : List[int]) -> List[int]:
        # code here
        meetings = sorted([(S[i], F[i], i+1) for i in range(N)], key=lambda x: (x[1], x[0]))
        res = [meetings[0][2]]
        last_finish = meetings[0][1]
        for s, f, i in meetings[1:]:
            if s > last_finish:
                res.append(i)
                last_finish = f
        return sorted(res)
