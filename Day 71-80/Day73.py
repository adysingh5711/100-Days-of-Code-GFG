# https://www.geeksforgeeks.org/problems/recamans-sequence4856/1


class Solution:
    def recamanSequence(self, n):
        a = [0] * n
        visited = set()

        for i in range(1, n):
            a[i] = a[i-1] - i

            # If the result is non-positive or already visited, add i instead
            if a[i] <= 0 or a[i] in visited:
                a[i] = a[i-1] + i

            visited.add(a[i])

        return a
