# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n):
        left = 1
        right = n

        while left < right:
            mid = left + (right - left) // 2

            if isBadVersion(mid):
                # mid could be the first bad version
                right = mid
            else:
                # First bad version must be after mid
                left = mid + 1

        return left