class Solution:
    def relativeSortArray(self, arr1, arr2):
        count = {}

        # Count elements in arr1
        for num in arr1:
            count[num] = count.get(num, 0) + 1

        result = []

        # Add elements in the order given by arr2
        for num in arr2:
            for _ in range(count[num]):
                result.append(num)
            del count[num]

        # Add remaining elements in ascending order
        for num in sorted(count):
            for _ in range(count[num]):
                result.append(num)

        return result