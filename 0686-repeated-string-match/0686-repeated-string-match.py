class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        repeats = (len(b) + len(a) - 1) // len(a)

        s = a * repeats

        if b in s:
            return repeats

        if b in s + a:
            return repeats + 1

        return -1