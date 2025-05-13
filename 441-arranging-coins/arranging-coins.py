class Solution(object):
    def arrangeCoins(self, n):
        if n == 1:
            return 1

        low = 0
        high = n

        mid = (low + high)//2
        ans = 0
        while low <= high:
            mid = (low + high)//2
            numcoins = (mid * (mid+1)//2)
            if numcoins <= n:
                ans = mid
                low = mid +1
            else:
                high = mid -1
        
        return ans
                
            
        
        



