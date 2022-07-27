# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        middle = (1 + n) // 2 
        left = 1
        right = n
        while left - right > 1:
            middle = (left + right) // 2 
            if isBadVersion(middle):
                right = middle
            else:
                left = middle
        return middle



# false, false, false, false, true, true, true

class Solution:
    def firstBadVersion(self, n: int) -> int:
        is_bad_previously = False
        first_bad_version = 1
        for current in range(1, n):
            is_bad_current = isBadVersion(current)
            if (not is_bad_previously and is_bad_current):
                first_bad_version = current
                break
            else:
                is_bad_previously = is_bad_current

        return first_bad_version
