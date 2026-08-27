class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        answer = [1] * n

        # Product of everything to the left
        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]

        # Product of everything to the right
        suffix = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]

        return answer