class Solution(object):
    def removePalindromeSub(self, s):
        if not s:
            return 0
        return 1 if s == s[::-1] else 2
        