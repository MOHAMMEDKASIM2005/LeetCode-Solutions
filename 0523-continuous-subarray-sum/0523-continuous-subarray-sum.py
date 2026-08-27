class Solution:
    def checkSubarraySum(self, nums, k):
        remainder_index = {0: -1}
        prefix_sum = 0

        for i, num in enumerate(nums):
            prefix_sum += num
            remainder = prefix_sum % k

            if remainder in remainder_index:
                # Need at least 2 elements
                if i - remainder_index[remainder] >= 2:
                    return True
            else:
                # Keep the earliest index for this remainder
                remainder_index[remainder] = i

        return False