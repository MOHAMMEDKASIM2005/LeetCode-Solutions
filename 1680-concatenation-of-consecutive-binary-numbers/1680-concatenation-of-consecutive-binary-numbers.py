class Solution:
    def concatenatedBinary(self, n: int) -> int:
        MOD = 10**9 + 7
        result = 0
        power = 1

        for i in range(1, n + 1):
            if i & (i - 1) == 0:
                power = (power * 2) % MOD

            result = (result * power + i) % MOD

        return result
        