class Solution:
    def longestDupSubstring(self, s: str) -> str:
        n = len(s)

        # Hash parameters
        base = 26
        mod = (1 << 61) - 1

        nums = [ord(c) - ord('a') for c in s]

        # Python implementation of modulo 2^61 - 1
        def mod_mul(a, b):
            x = a * b
            x = (x & mod) + (x >> 61)
            if x >= mod:
                x -= mod
            return x

        # Check whether a duplicate substring of length L exists
        def find_duplicate(L):
            if L == 0:
                return 0

            # base^(L-1)
            power = 1
            for _ in range(L - 1):
                power = mod_mul(power, base)

            # Hash of the first substring
            h = 0
            for i in range(L):
                h = (mod_mul(h, base) + nums[i] + 1) % mod

            seen = {h}

            for i in range(L, n):
                # Remove leftmost character
                h = (
                    h
                    - mod_mul(nums[i - L] + 1, power)
                ) % mod

                # Add new character
                h = (mod_mul(h, base) + nums[i] + 1) % mod

                if h in seen:
                    return i - L + 1

                seen.add(h)

            return -1

        left, right = 1, n - 1
        start = -1
        best_len = 0

        while left <= right:
            mid = (left + right) // 2
            idx = find_duplicate(mid)

            if idx != -1:
                best_len = mid
                start = idx
                left = mid + 1
            else:
                right = mid - 1

        if start == -1:
            return ""

        return s[start:start + best_len]