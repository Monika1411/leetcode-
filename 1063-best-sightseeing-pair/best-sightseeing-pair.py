class Solution(object):
    def maxScoreSightseeingPair(self, values):
        best = values[0] + 0
        result = 0
        for j in range(1, len(values)):
            result = max(result, best + values[j] - j)
            best = max(best, values[j] + j)
        return result
