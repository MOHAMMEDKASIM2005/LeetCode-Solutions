class Solution:
    def maxRepeating(self, sequence, word):
        k = 0
        repeated = word

        while repeated in sequence:
            k += 1
            repeated += word

        return k