class Solution:
    def subarraySum(self, nums, k):
        prefix_sum = 0
        count = 0

        # prefix_sum -> number of times it has appeared
        freq = {0: 1}

        for num in nums:
            prefix_sum += num

            # If prefix_sum - k exists, those previous prefix sums
            # form subarrays whose sum is exactly k.
            if prefix_sum - k in freq:
                count += freq[prefix_sum - k]

            freq[prefix_sum] = freq.get(prefix_sum, 0) + 1

        return count