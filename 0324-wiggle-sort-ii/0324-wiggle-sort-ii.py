class Solution:
    def wiggleSort(self, nums):
        nums.sort()

        n = len(nums)
        mid = (n + 1) // 2

        small = nums[:mid][::-1]
        large = nums[mid:][::-1]

        i = 0

        # Fill even indices: 0, 2, 4, ...
        for x in small:
            nums[i] = x
            i += 2

        i = 1

        # Fill odd indices: 1, 3, 5, ...
        for x in large:
            nums[i] = x
            i += 2