# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n

        while right - left > 1:
            middle = (left + right) // 2
            if isBadVersion(middle):
                right = middle
            else:
                left = middle

        return left + 1




# [false, false, false, false, true, true] -> 5
# [true] -> 1
# [false, false] -> 0

