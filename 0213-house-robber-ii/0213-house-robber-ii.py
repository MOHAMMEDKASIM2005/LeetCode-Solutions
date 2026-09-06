class Solution:

    def rob(self, nums):
        n = len(nums)  # Number of houses

        if n == 1:
            return nums[0]

        # Case 1:
        # First house considered, last house skipped
        case1 = self.robLinear(nums, 0, n - 2)

        # Case 2:
        # First house skipped, last house considered
        case2 = self.robLinear(nums, 1, n - 1)

        return max(case1, case2)

    def robLinear(self, nums, start, end):

        prev2 = 0  # Maximum money 2 houses back
        prev1 = 0  # Maximum money from previous house

        for i in range(start, end + 1):

            # Option 1: Skip current house
            # Option 2: Rob current house
            current = max(
                prev1,
                prev2 + nums[i]
            )

            prev2 = prev1
            prev1 = current

        return prev1