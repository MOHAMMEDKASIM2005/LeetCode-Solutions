class Solution:
    def findPeakElement(self, nums):
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[mid + 1]:
                # We are on a descending slope.
                # A peak exists at mid or to the left.
                right = mid
            else:
                # We are on an ascending slope.
                # A peak exists to the right.
                left = mid + 1

        return left