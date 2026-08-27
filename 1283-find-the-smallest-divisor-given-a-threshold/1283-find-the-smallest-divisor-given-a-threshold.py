class Solution:
    def smallestDivisor(self, nums, threshold):
        left = 1
        right = max(nums)

        while left < right:
            mid = (left + right) // 2

            total = 0
            for num in nums:
                # Ceiling division: ceil(num / mid)
                total += (num + mid - 1) // mid

            if total <= threshold:
                # mid works, try a smaller divisor
                right = mid
            else:
                # mid is too small
                left = mid + 1

        return left