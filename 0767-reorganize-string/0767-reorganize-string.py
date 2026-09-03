from collections import Counter
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:

        # Count frequency of each character
        freq = Counter(s)

        # Max heap using negative frequencies
        heap = []

        for char, count in freq.items():
            heapq.heappush(heap, (-count, char))

        result = []

        prev_count = 0
        prev_char = ""

        while heap:

            # Get most frequent character
            count, char = heapq.heappop(heap)

            # Add character to result
            result.append(char)

            # We used one occurrence
            count += 1

            # Put previous character back into heap
            if prev_count < 0:
                heapq.heappush(heap, (prev_count, prev_char))

            # Current character becomes previous
            prev_count = count
            prev_char = char

        # If not all characters were used
        if len(result) != len(s):
            return ""

        return "".join(result)