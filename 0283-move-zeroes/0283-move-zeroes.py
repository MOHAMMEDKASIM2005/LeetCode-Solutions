class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        insert_pos = 0

        # Move all non-zero elements to the front
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[insert_pos], nums[i] = nums[i], nums[insert_pos]
                insert_pos += 1
