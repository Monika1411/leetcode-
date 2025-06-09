class Solution(object):
    def maxScore(self, nums, x):
        dp_even = float('-inf')
        dp_odd = float('-inf')

        if nums[0] % 2 == 0:
            dp_even = nums[0]
        else:
            dp_odd = nums[0]

        for i in range(1, len(nums)):
            current = nums[i]
            parity = current % 2

            if parity == 0:
                same = dp_even + current
                diff = dp_odd + current - x
                dp_even = max(same, diff)
            else:
                same = dp_odd + current
                diff = dp_even + current - x
                dp_odd = max(same, diff)

        return max(dp_even, dp_odd)
