class Solution:
    def pancakeSort(self, arr):
        flips = []
        n = len(arr)

        for curr in range(n, 1, -1):
            # Find curr in the unsorted prefix
            idx = arr.index(curr, 0, curr)

            # Already in its correct position
            if idx == curr - 1:
                continue

            # Move curr to the front
            if idx != 0:
                arr[:idx + 1] = arr[:idx + 1][::-1]
                flips.append(idx + 1)

            # Move curr to its final position
            arr[:curr] = arr[:curr][::-1]
            flips.append(curr)

        return flips