class Solution:
    def subsetXORSum(self, nums):
        ans = 0

        for mask in range(1 << len(nums)):
            xor = 0

            for i in range(len(nums)):
                if mask & (1 << i):
                    xor = xor ^ nums[i]

            ans += xor

        return ans