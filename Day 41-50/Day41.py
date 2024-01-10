#https://www.geeksforgeeks.org/problems/longest-subarray-with-sum-divisible-by-k1259/1


class Solution:
	def longSubarrWthSumDivByK (self,arr,  n, k) : 
		#Complete the function
		total,ans = 0,0
		mp = dict()
		
		for i in range(n):
		    total += arr[i]
		    rem = total % k
		    
		    if rem == 0: ans = max(ans,i+1)
		    if rem not in mp:
		        mp[rem] = i
		    else:
		        ans = max(ans,i - mp[rem])
		
		return ans
