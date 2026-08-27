import random

class Solution:
    def findKthLargest(self, nums, k):
        target = len(nums) - k

        left = 0
        right = len(nums) - 1

        while left <= right:
            pivot = nums[random.randint(left, right)]

            # 3-way partition:
            # [less than pivot] [equal to pivot] [greater than pivot]
            lt = left
            i = left
            gt = right

            while i <= gt:
                if nums[i] < pivot:
                    nums[lt], nums[i] = nums[i], nums[lt]
                    lt += 1
                    i += 1

                elif nums[i] > pivot:
                    nums[i], nums[gt] = nums[gt], nums[i]
                    gt -= 1

                else:
                    i += 1

            if target < lt:
                right = lt - 1

            elif target > gt:
                left = gt + 1

            else:
                return nums[target]