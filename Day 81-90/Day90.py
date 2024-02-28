# https://www.geeksforgeeks.org/problems/check-if-a-number-is-divisible-by-83957/1


class Solution:
    def DivisibleByEight(self,s):
    # Extract the last three digits
        num_to_check = int(s[-3:]) if len(s) > 2 else int(s)
    # Check divisibility by 8
        if num_to_check % 8 == 0:
            return 1
        return -1
