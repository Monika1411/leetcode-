class Solution(object):
    def minOperations(self, grid, x):
        arr = sorted([num for row in grid for num in row])
        base = arr[0]
        for num in arr:
            if (num - base) % x != 0:
                return -1
        median = arr[len(arr) // 2]
        return sum(abs(num - median) // x for num in arr)
