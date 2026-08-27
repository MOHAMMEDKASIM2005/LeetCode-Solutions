class Solution:
    def frequencySort(self, s: str) -> str:
        count = {}

        # Count each character
        for ch in s:
            count[ch] = count.get(ch, 0) + 1

        # Sort characters by frequency (highest first)
        chars = sorted(count, key=count.get, reverse=True)

        # Build the result
        return ''.join(ch * count[ch] for ch in chars)