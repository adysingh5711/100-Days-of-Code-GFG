(* https://www.geeksforgeeks.org/problems/sum-of-bit-differences2937/1 *)


class Solution:
	def sumBitDifferences(self,arr, n):
    	# code here
    	ans = 0
    	for i in range(31, -1, -1):
    	    one = 0
    	    zero = 0
    	    for j in range(n):
    	        bit = 1 << i
    	        if (arr[j] & bit) > 0:
    	            one += 1
    	        else:
    	            zero += 1
    	    ans += (one * zero) * 2
    	return ans
