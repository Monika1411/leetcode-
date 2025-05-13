class Solution(object):
    def arrangeCoins(self, n):
        a=0
        while n>=a+1:
            a+=1
            n-=a
        return a

        