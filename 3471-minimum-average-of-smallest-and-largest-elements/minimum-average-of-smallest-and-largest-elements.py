class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        n = len(nums)
        s = sorted(nums)
        res = []
        
        for _ in range(n//2): 
            minv = s.pop(0)
            maxv = s.pop(-1)

            res.append((minv+maxv)/2)
        
        return min(res)